# -*- coding: utf-8 -*-
import scrapy
from mafengwo.items import MafengwoItem


class MfwSpider(scrapy.Spider):
    name = 'mfw'
    allowed_domains = ['www.mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/yj/10101/']

    def parse(self, response):
        travel_list=response.xpath('//div[@class="post-list"]/ul/li')
        for i_item in travel_list:
            mfw_item=MafengwoItem()
            mfw_item['title']=i_item.xpath('.//h2/a[@class="title-link"]/text()').extract_first()
            mfw_item['author']=i_item.xpath('.//span[@class="author"]/a[2]/text()').extract_first()
            mfw_item['ding']=i_item.xpath('.//div[@class="post-ding"]/span/text()').extract_first()
            content=i_item.xpath('.//div[@class="post-content"]/text()').extract_first()
            mfw_item['content']=''.join(content.split())
            mfw_item['img_url']=i_item.xpath('.//div[@class="post-cover"]//img/@data-original').extract_first()
            yield mfw_item

        next_link=response.xpath('//div[@class="page-hotel"]/a[contains(@class,"next")]/@href').extract()
        #下一页
        if next_link:
            next_link=next_link[0]
            yield scrapy.Request('http://www.mafengwo.cn/'+next_link,callback=self.parse)
