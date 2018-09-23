# coding:utf-8
import re
import requests
import json
import time

# headers = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive',
#     'Host': '36kr.com',
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
# }

# response = requests.get('https://36kr.com/p/5134929.html', headers=headers)

# article_id = scrapy.Field()
# article_url = scrapy.Field()
# article_title = scrapy.Field()
# article_summary = scrapy.Field()
# article_content = scrapy.Field()
# writer_name = scrapy.Field()
# column_name = scrapy.Field()
# writer_role = scrapy.Field()
# published_time = scrapy.Field()
# crawled_time = scrapy.Field()

# with open('detail_36kr.html', 'r') as f:
with open('error_36kr.html', 'r') as f:
    article = f.read()
    # print(article)
    # pattern = re.compile('<script>var props=({.*?)</script>')
    pattern = re.compile('\s*<script>var props={"detailArticle\|post":(.*?)\s*},\s*locationnal\s*=\s*')
    content = pattern.findall(article, re.S)[0]
    # print(content)
    data = json.loads(content)
    # print(data)

    items = {}
    field_map = {
        'article_id': 'id',
        'published_time': 'published_at',
        'article_title': 'title',
        'article_summary': 'summary',
        'article_tags': 'extraction_tags',
        'article_content': 'content',
    }
    #
    for field, attr in field_map.items():
        items[field] = data.get(attr)
    #
    items['column_name'] = data.get('column').get('name')
    items['writer_name'] = data.get('user').get('name')
    items['writer_role'] = data.get('user').get('title')
    tag = re.sub(r'\d+\],?|\[|\]|\"', '', items['article_tags'])
    article_content = re.sub(r'<a.*?>|</a>|<img.*?><p class="img-desc">.*?</p>|<p>|</p>|<br.*?>|\n|\t|\s', '',
                             items.get('article_content'))
    # print(time.localtime())
    print(items)
