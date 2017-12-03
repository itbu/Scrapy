# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LagouItem(scrapy.Item):
    #链接
    url = scrapy.Field()
    #职位名称
    job_name = scrapy.Field()
    #开始工资
    smoney = scrapy.Field()
    #结束工资
    emoney = scrapy.Field()
    #地址
    location = scrapy.Field()
    #经验开始
    syear = scrapy.Field()
    #经验结束
    eyear = scrapy.Field()
    #学历
    degree = scrapy.Field()
    #标签
    tags = scrapy.Field()
    #招聘时间
    date_pub = scrapy.Field()
    #职位诱惑/福利
    welfare = scrapy.Field()
    #工作信息详情
    jobdesc = scrapy.Field()
    #工作地址
    jobaddr = scrapy.Field()
    #公司详情
    company_desc = scrapy.Field()
    #公司名称
    company = scrapy.Field()
    #来源
    source = scrapy.Field()
    #抓取时间
    crawl_time = scrapy.Field()
