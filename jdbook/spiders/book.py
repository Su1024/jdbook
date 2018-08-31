# -*- coding: utf-8 -*-
import requests
import scrapy
import json

from jdbook.items import JdbookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.jd.com', 'list.jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        # 解析出 图书的url
        tar_url = response.xpath('//div[@class="mc"]//dd')
        for url in tar_url:
            item = JdbookItem()
            book_url = "https:" + url.xpath('.//a/@href').extract_first()
            item['category'] = url.xpath('.//a/text()').extract_first()
            item['tar_url'] = book_url
            yield scrapy.Request(
                url=book_url,
                callback=self.parse_detail,
                meta={
                    'item': item
                }
            )

    def parse_detail(self, repsonse):
        item = repsonse.meta['item']

        li_list = repsonse.xpath('//li[@class="gl-item"]')
        for li in li_list:
            name = li.xpath('.//div[@class="p-name"]//em/text()').extract_first().strip()
            id = li.xpath('./div/@data-sku').extract_first()
            price = self.get_book_price(id)
            item['name'] = name
            item['price'] = price
            # price = li.xpath('.//div[@class="p-price"]//i/text()').extract_first()
            yield item

    def get_book_price(self, sku_id):
        price_url = "http://p.3.cn/prices/mgets?skuIds=J_" + sku_id
        resp = requests.get(price_url)
        sku_dict = json.loads(resp.text)[0]
        return sku_dict['p']
