# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbookItem(scrapy.Item):
    # 图书分类
    category = scrapy.Field()
    # 链接
    tar_url = scrapy.Field()
    # 图书名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
