from scrapy import  cmdline
import os
os.chdir('zh/spiders')

cmdline.execute('scrapy runspider chinahr.py'.split())