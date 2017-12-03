# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
from scrapy_redis.spiders import RedisCrawlSpider

def get_num(strs):
    pattern = re.compile(r'\d+')
    m = pattern.findall(strs)
    return m

def get_date_pub(date_pub):
    if '今天' in date_pub:
        date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
    elif '昨天' in date_pub:
        date_pub = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        date_pub = '-'.join(get_num(date_pub))
    return  date_pub

def get_year(year):
    if get_num(str(year)):
        year = get_num(str(year))[0]
    else:
        year = 0
    return year

class ChinahrSpider(RedisCrawlSpider):
    name = 'chinahr'
    allowed_domains = ['chinahr.com']
    # start_urls = ['http://www.chinahr.com/']
    redis_key = "ChinahrSpider:start_urls"

    rules = (
        # Rule(LinkExtractor(allow=r'/sou/'), follow=True),
        Rule(LinkExtractor(allow=r'/\w+/jobs/\d+/'), follow=True),

        Rule(LinkExtractor(allow=r'/job/\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        url = response.url
        job_name = response.xpath('//div[@class="job-detail-l"]//h1/span[1]/text()').extract_first()
        money = response.xpath('//span[@class="job_price"]/text()').extract_first()
        money = get_num(money)
        if len(money) == 2:
            # money = '-'.split(money)
            smoney = int(float(money[0]) /1000)
            emoney = int(float(money[1])/1000)
        else:
            emoney = 0
            smoney = 0
        print(smoney,emoney)
        location = response.xpath('//div[@class="base_info"]//div[@class="job_require"]/span[2]/text()').extract_first()
        year = response.xpath('//span[@class="job_exp"]/text()').extract_first()
        syear= get_year(year)
        eyear = get_year(year)
        degree =response.xpath('//div[@class="job_require"]/span[4]/text()').extract_first()
        tags =response.xpath('//div[@class="compny_tag"]/span/text()').extract()
        tags = ','.join(tags)
        date_pub =response.xpath('//p[@class="updatetime"]/text()').extract_first()
        welfare =response.xpath('//ul[@class="clear"]/li/text()').extract_first()
        jobdesc =response.xpath('//div[@class="job_intro_info"]/text()').extract()
        jobdesc = ','.join(jobdesc).strip()
        jobaddr =response.xpath('//span[@class="job_loc"]/text()').extract_first()
        company_desc =''.join(response.xpath('//div[@class="company_service"]/text()').extract())
        company =response.xpath('//div[@class="job-company jrpadding"]/h4/a/text()').extract_first()
        if 'china' in  response.url:
            source = '中华英才'
        else:
            source = '其他网站'
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        # print(url,job_name,smoney,emoney,location,syear,eyear,degree,tags,date_pub,welfare,jobdesc,jobaddr,company_desc,company,source,crawl_time)
        yield {
            'url': url,
            'job_name': job_name,
            'smoney': smoney,
            'emoney': emoney,
            'location': location,
            'syear': syear,
            'eyear': eyear,
            'degree': degree,
            'tags': tags,
            'date_pub': date_pub,
            'welfare': welfare,
            'jobdesc': jobdesc,
            'jobaddr': jobaddr,
            'company_desc': company_desc,
            'company': company,
            'source': source,
            'crawl_time': crawl_time
        }
