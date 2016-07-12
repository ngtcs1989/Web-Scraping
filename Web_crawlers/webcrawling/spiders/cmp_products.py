# -*- coding: utf-8 -*-
import scrapy
from webcrawling.items import *

class CmpProductsSpider(scrapy.Spider):
    name = "cmp_products"
    allowed_domains = ["amazon.com"]
    start_urls = (
            'http://www.amazon.com/',
            )
    def product_page(self, response):
        prices = response.xpath('//a[@class="a-link-normal a-text-normal"]/span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract()
        #prices = response.xpath('//a[@class="a-link-normal a-text-normal"]').extract()
        print(prices)
    def parse(self, response):
        yield scrapy.FormRequest.from_response(
                response,
                formxpath="//form[@name='site-search']",
                formdata={
                    "field-keywords":"shoes",
                    },
                clickdata = { "type": "submit" },
                callback=self.product_page
                ) 
