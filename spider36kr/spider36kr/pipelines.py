# -*- coding: utf-8 -*-

from spider36kr.items import Spider36KrItem
import re
import logging
import pymongo
import pymysql
import redis
from scrapy.exceptions import DropItem


class Spider36KrPipeline(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        if isinstance(item, Spider36KrItem):
            if item.get('article_tags'):
                item['article_tags'] = self.parse_tags(item.get('article_tags'))
            if item.get('article_content'):
                item['article_content'] = self.parse_content(item.get('article_content'))
            if item.get('article_summary'):
                item['article_summary'] = item.get('article_summary').replace(' ', '')
            if item.get('article_title'):
                item['article_title'] = item.get('article_title').replace(' ', '')
            if item.get('writer_role') == '读者':
                item['writer_role'] = ''
        return item

    def parse_tags(self, origin_tags):
        tag = re.sub(r'\d+\],?|\[|\]|\"', '', origin_tags).rstrip(',')
        tags = eval("u" + "\'" + tag + "\'")
        return tags

    def parse_content(self, origin_content):
        article_content = re.sub(r'<a.*?>|</a>|<img.*?>|<p class="img-desc">.*?</p>|<p>|</p>|<br.*?>|\n|\t|\s', '',
                                 origin_content)
        return article_content


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.logger = logging.getLogger(__name__)
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        if isinstance(item, Spider36KrItem):
            self.db[item.collection].update({'article_id': item.get('article_id')}, {'$set': dict(item)}, True)
            self.logger.info('ID: %s 的新闻已经插入到mogondb中' % item.get('article_id'))
        return item

    def close_spider(self, spider):
        self.client.close()


class RedisPipeline(object):
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('REDIS_HOST'),
            port=crawler.settings.get('REDIS_PORT'),
            db=crawler.settings.get('REDIS_DB')
        )

    def open_spider(self, spider):
        self.redis_db = redis.StrictRedis(self.host, self.port, self.db, decode_responses=True)

    def process_item(self, item, spider):
        redis_data_url = {'36kr': 'url'}
        if self.redis_db.hexists(redis_data_url, item.get('article_url')):
            raise DropItem("Duplicate item found:%s" % item.get('article_url'))
        else:
            self.redis_db.hset(redis_data_url, item.get('article_url'), 0)
            return item
