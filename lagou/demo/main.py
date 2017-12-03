from scrapy import cmdline
import os

os.chdir('demo/spiders')
cmdline.execute('scrapy runspider lagou.py'.split())