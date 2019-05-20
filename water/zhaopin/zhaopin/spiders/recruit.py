# -*- coding: utf-8 -*-
import scrapy
from zhaopin.items import ZhaopinItem

class RecruitSpider(scrapy.Spider):
    name = 'recruit'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://jobs.zhaopin.com/jinan/']

    def parse(self, response):
        #print(response.body.decode())
        detailobjs = response.xpath("//div[@class='details_container bg_container ']")
        #print("detailobjs:::::",detailobjs)
        #lst = list()
        i=0
        for detailobj in detailobjs:
            item = ZhaopinItem()
            zhiwei = detailobj.xpath("//span[@class='post']/a/text()")[i].extract()
            zhiwei_url = detailobj.xpath("//span[@class='post']//a/@href")[i].extract()
            gongsi = detailobj.xpath("//span[@class='company_name']/a/text()")[i].extract()
            gongsi_url = detailobj.xpath("//span[@class='company_name']/a/@href")[i].extract()
            yuexin = detailobj.xpath("//span[@class='salary']/text()")[i].extract()
            gongzuodidian = detailobj.xpath("//span[@class='address']/text()")[i].extract()
            faburiqi = detailobj.xpath("//span[@class='release_time']/text()")[i].extract()

            item['zhiwei'] = zhiwei
            item['zhiwei_url'] = zhiwei_url
            item['gongsi'] = gongsi
            item['gongsi_url'] = gongsi_url
            item['yuexin'] = yuexin
            item['gongzuodidian'] = gongzuodidian
            item['faburiqi'] = faburiqi
            #lst.append(item)
            i+=1
            yield item
        # print(lst)
        # return lst
