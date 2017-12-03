# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql


class DemoPipeline(object):
    def process_item(self, item, spider):
        return item

class TencentPipeline(object):
    def __init__(self):
        self.f = open('postion.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item

    def close_spider(self,spider):
        self.f.close()



class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','temp',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class LagouMysqlPipline(MysqlPipeline):
    def process_item(self,item,spider):
        if spider.name == 'lagou':
            sql = 'insert into aaa(url,job_name,smoney,emoney,location,syear,eyear,degree,tags,date_pub,welfare,jobdesc,jobaddr,company_desc,company,source,crawl_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update date_pub=values(date_pub),smoney=VALUES(smoney),emoney=values(emoney)'
            try:
                self.cursor.execute(sql, (item["url"], item["job_name"], item["smoney"], item["emoney"], item["location"], item["syear"],item["eyear"], item["degree"],item["tags"], item["date_pub"], item["welfare"],item["jobdesc"], item["jobaddr"], item["company"], item["crawl_time"]))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print("执行语句失败")

            return item





