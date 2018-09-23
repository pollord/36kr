# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import time
import json
import re
from spider36kr.items import Spider36KrItem


class A36krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['36kr.com']
    # page页码，keyword搜索关键词， time_stamp时间戳
    search_url = 'https://36kr.com/api//search/entity-search?page={page}&per_page=40&keyword={keyword}&entity_type=post&sort=date&_={time_stamp}'
    # .format(page, keyword, time_stamp)
    detail_url = 'https://36kr.com/p/{article_id}.html'
    # urlencode 转的是字典
    keyword = urlencode({'keyword': '区块链'}).split('=')[-1]
    # keyword = '%E5%8C%BA%E5%9D%97%E9%93%BE'
    page = 30

    def start_requests(self):
        # self.logger.debug(self.keyword)
        time_stamp = str(int(time.time()*1000))
        yield scrapy.Request(self.search_url.format(page=self.page, keyword=self.keyword, time_stamp=time_stamp),
                             callback=self.parse_url)

    def parse_url(self, response):
        result = json.loads(response.text)
        # 最后一页的json数据没有items
        if result.get('data').get('items'):
            self.page += 1
            time_stamp = str(int(time.time() * 1000))
            yield scrapy.Request(self.search_url.format(page=self.page, keyword=self.keyword, time_stamp=time_stamp),
                                 callback=self.parse_url)

            articles_info = result.get('data').get('items')
            for article in articles_info:
                article_id = article.get('id')
                yield scrapy.Request(self.detail_url.format(article_id=article_id), callback=self.parse_detail,
                                     dont_filter=True)

    def parse_detail(self, response):
        self.logger.debug(response.headers)
        try:
            result = re.findall('<script>var props={"detailArticle\|post":(.*?),\s*"hotPostsOf30\|hotPost"\:\s*\[{',
                                response.text, re.S)[0]

        except IndexError:
            # self.logger.error(response.text)
            result = re.findall('\s*<script>var props={"detailArticle\|post":(.*?)\s*},\s*locationnal\s*=\s*',
                                response.text, re.S)[0]
        else:
            data = json.loads(result)
            item = Spider36KrItem()
            field_map = {
                'article_id': 'id', 'article_title': 'title', 'article_summary': 'summary', 'article_content': 'content',
                'published_time': 'published_at', 'article_tags': 'extraction_tags',
            }

            for field, attr in field_map.items():
                item[field] = data.get(attr)
            item['article_url'] = response.url
            item['column_name'] = data.get('column').get('name')
            item['writer_name'] = data.get('user').get('name')
            item['writer_role'] = data.get('user').get('title')
            item['crawled_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            yield item




