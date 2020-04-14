# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class mobile_item(scrapy.Item):
    # define the fields for your item here like:
    smartphone_name = scrapy.Field()
    smartphone_price = scrapy.Field()
    smartphone_rating = scrapy.Field()
    percentage_off = scrapy.Field()


