# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #游记题目
    title=scrapy.Field()
    #游记作者
    author=scrapy.Field()
    #游记顶数
    ding=scrapy.Field()
    #游记简介
    content=scrapy.Field()
    #游记图片地址
    img_url=scrapy.Field()
