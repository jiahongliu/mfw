# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MafengwoPipeline(object):
    def process_item(self, item, spider):
        return item

class mfwMYSQLPipeline(object):
    def process_item(self, item, spider):
        con = pymysql.connect(host='localhost', port=3306, user='root', passwd='jjjj', db='spiders', charset='utf8')
        cur = con.cursor()
        sql = 'INSERT INTO blog_travel(title,author,ding,content,img_url) VALUES (%s,%s,%s,%s,%s)'
        lis=(
            item['title'],
            item['author'],
            item['ding'],
            item['content'],
            item['img_url'],
        )
        try:
            if cur.execute(sql,lis):
                print('successful')
                con.commit()
        except:
            print('Failed')
            cur.rollback()
        cur.close()
        con.close()
        return item
