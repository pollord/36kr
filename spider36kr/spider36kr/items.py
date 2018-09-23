# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider36KrItem(scrapy.Item):
    collection = table = '36krb'
    article_id = scrapy.Field()
    article_url = scrapy.Field()

    article_title = scrapy.Field()
    article_summary = scrapy.Field()
    article_content = scrapy.Field()
    article_tags = scrapy.Field()

    writer_name = scrapy.Field()
    column_name = scrapy.Field()
    writer_role = scrapy.Field()

    published_time = scrapy.Field()
    crawled_time = scrapy.Field()


# class ArticleItem(scrapy.Item):
#     article_id = scrapy.Field()
#     article_url = scrapy.Field()
#     article_title = scrapy.Field()
#     article_summary = scrapy.Field()
#     article_content = scrapy.Field()
#
#     article_tags = scrapy.Field()
#     column_name = scrapy.Field()
#
#     crawled_time = scrapy.Field()
#
#
# class WriterItem(scrapy.Item):
#     writer_name = scrapy.Field()
#     writer_role = scrapy.Field()
#     published_time = scrapy.Field()
#
