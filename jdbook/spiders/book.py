# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.jd.com']
    start_urls = ['http://book.jd.com/']

    def parse(self, response):
        pass
