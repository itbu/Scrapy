# -*- coding: utf-8 -*-
import json
import redis  # pip install redis
import pymysql

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.191.128', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='temp',port=3307, charset='utf8',)

    # 无限循环
    while True:
        source, data = rediscli.blpop(["chinahr:items"]) # 从redis里提取数据

        item = json.loads(data.decode('utf-8')) # 把 json转字典

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            sql = 'insert into job (url,job_name,smoney,emoney,location,syear,eyear,degree,tags,date_pub,welfare,jobdesc,jobaddr,company_desc,company,source,crawl_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update date_pub=values(date_pub),smoney=VALUES(smoney),emoney=values(emoney)'
            cur.execute(sql, (item['url'],item['job_name'],item['smoney'],item['emoney'],item['location'],item['syear'],item['eyear'],item['degree'],item['tags'],item['date_pub'],item['welfare'],item['jobdesc'],item['jobaddr'],item['company_desc'],item['company'],item['source'],item['crawl_time']))

            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print ("插入 %s" % item['job_name'])
        except pymysql.Error as e:
            mysqlcli.rollback()
            print ("插入错误" ,str(e))

if __name__ == '__main__':
    main()