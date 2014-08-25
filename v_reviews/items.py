# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    date = scrapy.Field()
    rate = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
    museum = scrapy.Field()
