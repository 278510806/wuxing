# -*- coding: utf-8 -*-

import scrapy
from zhaopin.items import ZhaopinItem


class RecruitSpider(scrapy.Spider):
    name = 'recruit'
    allowed_domains = ['zhaopin.com']

    location_list = ["beijing", "shanghai", "guangzhou", "shenzhen"
        , "tianjin", "wuhan", "xian", "chengdu", "dalian", "changchun"
        , "shenyang", "nanjing", "jinan", "qingdao", "hangzhou", "suzhou"
        , "wuxi", "ningbo", "chongqing", "zhengzhou", "changsha", "fuzhou"
        , "xiamen", "haerbin", "shijiazhuang", "hefei", "huizhou"
        , "taiyuan", "kunming", "yantai", "foshan", "nanchang", "guiyang"]
    base_url = 'http://jobs.zhaopin.com/{location}/p{num}/'
    num = 1
    cnt = 0
    # location=location_list[0]
    start_urls = [base_url.format(num=num, location=location_list[cnt])]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,errback=self.parse_error)
    def parse_error(self,response):
        print("::::::::::::::::::::::::",response.status)
    def parse(self, response):
        # notfound = response.xpath("//div[@class='returnpage']/h1/text()")
        # print("notfound", notfound)
        if response.status != 404:
            detailobjs = response.xpath("//div[@class='details_container bg_container ']")
            i = 0
            for detailobj in detailobjs:
                item = ZhaopinItem()
                zhiwei = detailobj.xpath("//span[@class='post']/a/text()")[i].extract()
                zhiwei_url = detailobj.xpath("//span[@class='post']//a/@href")[i].extract()
                gongsi = detailobj.xpath("//span[@class='company_name']/a/text()")[i].extract()
                gongsi_url = detailobj.xpath("//span[@class='company_name']/a/@href")[i].extract()
                yuexin = detailobj.xpath("//span[@class='salary']/text()")[i].extract()
                gongzuodidian = detailobj.xpath("//span[@class='address']/text()")[i].extract()
                faburiqi = detailobj.xpath("//span[@class='release_time']/text()")[i].extract()
                gongzuojingyan = detailobj.xpath("//div[@class='fleft detail_items']/span[1]/text()")[0].extract()
                gongzuojingyan = gongzuojingyan.split("：")[1]
                xueli = detailobj.xpath("//div[@class='fleft detail_items']/span[2]/text()")[0].extract()
                xueli = xueli.split("：")[1]
                gongsiguimo = detailobj.xpath("//div[@class='fleft detail_items']/span[3]/text()")[0].extract()
                gongsiguimo = gongsiguimo.split("：")[1]
                gongsixingzhi = detailobj.xpath("//div[@class='fleft detail_items']/span[4]/text()")[0].extract()
                gongsixingzhi = gongsixingzhi.split("：")[1]

                item['zhiwei'] = zhiwei
                item['zhiwei_url'] = zhiwei_url
                item['gongsi'] = gongsi
                item['gongsi_url'] = gongsi_url
                item['yuexin'] = yuexin
                item['gongzuodidian'] = gongzuodidian
                item['faburiqi'] = faburiqi
                item['gongzuojingyan'] = gongzuojingyan
                item['xueli'] = xueli
                item['gongsiguimo'] = gongsiguimo
                item['gongsixingzhi'] = gongsixingzhi
                item['location'] = self.location_list[self.cnt]
                i += 1
                yield item
            self.num += 1
            url = self.base_url.format(num=self.num, location=self.location_list[self.cnt])
            yield scrapy.Request(url, callback=self.parse)
        else:
            print("===============================================================================")
            if self.cnt < len(self.location_list) - 1:
                # time.sleep(random.uniform(1, 5))
                self.num = 1
                self.cnt += 1
                url = self.base_url.format(num=self.num, location=self.location_list[self.cnt])
                yield scrapy.Request(url, callback=self.parse)
