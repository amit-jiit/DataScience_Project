# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewswebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title_link = scrapy.Field()

    # for new_article.py
    title = scrapy.Field()
    summary = scrapy.Field()
    author = scrapy.Field()
    like_facebook = scrapy.Field()
    tags = scrapy.Field()
    date = scrapy.Field()


