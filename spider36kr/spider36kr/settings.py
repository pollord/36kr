# -*- coding: utf-8 -*-

# Scrapy settings for spider36kr project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'spider36kr'

SPIDER_MODULES = ['spider36kr.spiders']
NEWSPIDER_MODULE = 'spider36kr.spiders'

MONGO_URI = 'localhost'
MONGO_DB = '36kr'


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
REDIS_DB = 2


MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'mysql'
MYSQL_DATABASE = '36kr'

from datetime import datetime
today = datetime.now()
log_file_path = 'log/scrapy_{}_{}_{}.log'.format(today.year, today.month, today.day)

# LOG_LEVEL = 'DEBUG'
# LOG_FILE = log_file_path


PROXY_URL = 'http://localhost:5555/random'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider36kr (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.randint(1, 3)
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=b65cfd2215372483927264609e1428e6ffb62513e1d939a5ffd18f894ed468; device-uid=674ee5c0-bb03-11e8-93c1-f1c0823e8b5d; sajssdk_2015_cross_new_user=1; kr_stat_uuid=yxHat25620806; Hm_lvt_713123c60a0e86982326bae1a51083e1=1537246341; Hm_lvt_1684191ccae0314c6254306a8333d090=1537246341; download_animation=1; Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3=1537248424; Hm_lpvt_e8ec47088ed7458ec32cde3617b23ee3=1537248424; krnewsfrontss=7ecf44760023315d4b7bf75c8c7b562a; M-XSRF-TOKEN=28fc74ef6891c5e297dd25bcc7da014c1aa280cd009c5993022aafe0b93d3bf0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22yxHat25620806%22%2C%22%24device_id%22%3A%22165eb24f5ba188-062dae1752f4b2-762e6d31-327015-165eb24f5bb2f1%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%22165eb24f5ba188-062dae1752f4b2-762e6d31-327015-165eb24f5bb2f1%22%7D; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1537256032; Hm_lpvt_1684191ccae0314c6254306a8333d090=1537256032',
    'Host': '36kr.com',
    # 'Referer': 'https://36kr.com/search/articles/%E5%8C%BA%E5%9D%97%E9%93%BE?page=2&ts=1537247606603',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
    # 'X-Tingyun-Id': 'Dio1ZtdC5G4;r=256032302',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spider36kr.middlewares.Spider36KrSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'spider36kr.middlewares.Spider36KrDownloaderMiddleware': 543,
    'spider36kr.middlewares.ProxyMiddleware': 554,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spider36kr.pipelines.Spider36KrPipeline': 543,
    'spider36kr.pipelines.MongoPipeline': 545,
    # 'spider36kr.pipelines.MysqlPipeline': 546,
    'spider36kr.pipelines.RedisPipeline': 544,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
