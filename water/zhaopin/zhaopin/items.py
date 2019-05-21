# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    zhiwei=scrapy.Field()
    zhiwei_url=scrapy.Field()
    gongsi=scrapy.Field()
    gongsi_url=scrapy.Field()
    yuexin=scrapy.Field()
    gongzuodidian=scrapy.Field()
    faburiqi=scrapy.Field()
    gongzuojingyan=scrapy.Field()
    xueli=scrapy.Field()
    gongsiguimo=scrapy.Field()
    gongsixingzhi=scrapy.Field()
    location=scrapy.Field()
