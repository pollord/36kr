# -*- coding: utf-8 -*-
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
