# -*- coding: utf-8 -*-

# Scrapy settings for demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'demo'

SPIDER_MODULES = ['demo.spiders']
NEWSPIDER_MODULE = 'demo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 6

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Host": "www.lagou.com",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cookie": "user_trace_token=20170928185746-dc78913e-a43b-11e7-932b-5254005c3644; LGUID=20170928185746-dc7893d2-a43b-11e7-932b-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=07ec21c9a0b55e9375abae536a4d16d2; JSESSIONID=ABAAABAABEEAAJA74F9F5EF3BD986A902C52B65C429D193; _gid=GA1.2.650195424.1510819141; _gat=1; _ga=GA1.2.1653106244.1506596267; LGSID=20171116165957-8554e187-caac-11e7-98fd-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171116165957-8554e2d2-caac-11e7-98fd-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510229311,1510819139; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510822789",
    # "Cookie":"user_trace_token=20171116161309-fb3b03da-caa5-11e7-98fb-5254005c3644; LGUID=20171116161309-fb3b0666-caa5-11e7-98fb-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=2531adeeeb338c27e8ab799021db6534; SEARCH_ID=3579802e9e8647439b2e8eb3cbc66876; TG-TRACK-CODE=index_bannerad; JSESSIONID=ABAAABAABEEAAJA94C0DC800DC4DD62C4590ABED7ECAAB4; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510819989,1510820787; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510842415; _gid=GA1.2.1891807880.1510819990; _ga=GA1.2.479871929.1510819989; LGSID=20171116222642-2a716213-cada-11e7-9913-5254005c3644; LGRID=20171116222656-32de626e-cada-11e7-936f-525400f775ce",
}


                                            # Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'demo.middlewares.DemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'demo.middlewares.RandomUserAgent': 1,
    'demo.middlewares.FreeRandomProxy': 2,
    'demo.middlewares.AuthRandomProxy': 3,
}

# DOWNLOADR_MIDDLEWARES = 10
DOWNLOAD_TIMEOUT = 5
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'demo.pipelines.TencentPipeline': 300,
    'demo.pipelines.LagouMysqlPipline': 1,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

RANDOM_UA_TYPE = 'random'


PROXIES = [
    {'host':'39.106.122.107:8888'},
    {'host':'110.73.2.87:8123'},
    {'host':'119.36.92.46:81'},
    {'host':'182.92.242.11:80'},
    {'host':'120.27.233.197:80'},
    {'host':'27.46.53.13:8118'},
    {'host':'39.104.15.241:8080'},
    {'host':'122.96.59.105:83'},
    {'host':'121.196.226.246:84'},
    {'host':'118.193.107.20:80'},
    {'host':'111.59.132.252:8123'},
    {'host':'220.174.209.230:8123'},
    {'host':'116.199.2.208:80'},
    {'host':'111.56.5.42:80'},
    {'host':'39.104.14.119:8080'},
    {'host':'118.178.227.171:80'},
    {'host':'121.232.146.58:9000'},
    {'host':'118.193.107.186:80'},
    {'host':'118.193.107.2:80'},
    {'host':'119.36.92.47:81'},
    {'host':'118.193.107.40:80'},
    {'host':'39.108.171.142:80'},
    {'host':'106.14.225.18:8082'},
    {'host':'118.193.107.37:80'},
    {'host':'182.141.60.80:9000'},
    {'host':'119.36.92.46:80'},
    {'host':'112.13.93.43:8088'},
    {'host':'118.193.107.192:80'},
    {'host':'118.114.77.47:8080'},
    {'host':'118.193.107.101:80'},
    {'host':'223.96.95.229:3128'},
]

AUTH_PROXIES = [
    {'host':'120.78.166.84:6666','auth':'alice:123456'}
]

# url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}

# redis连接配置
REDIS_HOST = '192.168.137.128'
REDIS_PORT = 6379

