import scrapy


from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
import re
import datetime
from datetime import timedelta
from demo.items import LagouItem
from scrapy_redis.spiders import RedisCrawlSpider

class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    # start_urls = ['https://www.lagou.com']
    redis_key = 'lagouspider:urls'

    rules = (
        Rule(LinkExtractor(allow =r'zhaopin/.*'),follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'),follow=True),
        Rule(LinkExtractor(allow=r'jobs/list_.*'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=False),

    )
    num_pattern = re.compile(r'\d+')
    def parse_item(self,response):
        # print(response.url)
        item = LagouItem()
        #链接
        url = response.url
        #职位名称
        job_name = response.css('.job-name::attr(title)').extract()[0]
        #工资
        money = response.css('.job_request .salary::text').extract()[0]
        smoney = money.lower().replace('k','').split('-')[0]
        emoney = money.lower().replace('k', '').split('-')[1]
        #地址
        location = response.xpath('//*[@class="job_request"]/p/span[2]/text()').extract()[0]
        location = self.remove_splash(location)

        #经验
        year = response.xpath('//*[@class="job_request"]/p/span[3]/text()').extract()[0]
        syear ,eyear = self.process_year(year)
        #学历
        degree = response.xpath('//*[@class="job_request"]/p/span[4]/text()').extract()[0]
        degree = self.remove_splash(degree)

        #标签
        tags = response.css('.position-label li::text').extract()
        tags = ','.join(tags)
        #招聘时间
        date_pub = response.css('.publish_time::text').extract()[0]
        date_pub = self.process_date(date_pub)
        #职位诱惑/福利
        welfare = response.css('.job-advantage p::text').extract()[0]
        #工作信息详情
        jobdesc = response.css('.job_bt div p::text').extract()
        jobdesc = ''.join(jobdesc)
        #工作地址
        jobaddr1 = response.css('.work_addr a::text').extract()[:-1]
        jobaddr2 = response.css('.work_addr::text').extract()[-2].strip()
        jobaddr = ''.join(jobaddr1) + jobaddr2
        #公司详情
        company_desc=response.xpath('//ul[@class="c_feature"]/li[1]/text()').extract()[-2].strip()
        #公司名称
        company = response.css('#job_company dt a img::attr(alt)').extract()[0]
        #来源
        # source =response.xpath('//ul[@class="c_feature"]//a[@rel="nofollow"]/text()').extract()[0]
        if 'laguo' in response.url:
            source='拉勾'
        else:
            source = '其他网站'
        #爬取时间
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')

        item['url'] = url
        item['job_name'] = job_name
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['company_desc'] = company_desc
        item['tags'] = tags
        item['date_pub'] = date_pub
        item['welfare'] = welfare
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['source'] = source
        item['crawl_time'] = crawl_time

        yield item

    def process_date(self,value):
        if '天前' in value:
            res = self.num_pattern.search(value).group()
            date_pub = (datetime.datetime.now() - timedelta(days=int(res))).strftime('%Y-%m-%d')
        else:
            date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        return date_pub

    def process_year(self,year):
        if '-' in year:
            res = self.num_pattern.findall(year)
            syear = res[0]
            eyear = res[1]
        elif '以上' in year:
            res = self.num_pattern.search(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0
        return syear,eyear

    def remove_splash(self,value):
        return value.replace('/','').strip()
