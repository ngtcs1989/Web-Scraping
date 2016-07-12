# -*- coding: utf-8 -*-
import scrapy
from webcrawling.items import *

class MasseffectSpider(scrapy.Spider):
    name = "massEffect"
    allowed_domains = ["tfaw.com"]
    start_urls = (
        'http://www.tfaw.com/Companies/Dark-Horse/Series?series_name=Massive',
    )

    def parse(self, response):
        #print (response.xpath('//a[@class="regularlinksmallbold product-profile-link"]/@href').extract())
        for i in response.xpath('//a[@class="regularlinksmallbold product-profile-link"]/text()').extract():
            url = response.urljoin(i)
            yield scrapy.Request(url, callback=self.parse_detail_page)
        #pass

    def parse_detail_page(self, response):
    	data = WebcrawlingItem()
    	data['title'] = response.xpath('//span[@class="blackheader" and @itemprop="name"]/text()').extract()
    	#data['price'] = response.css('span.blackheader ~ span.redheader::text').re('[$]\d+\.\d+')
    	#data['upc'] = response.xpath(‘...’).extract()
    	#data['url'] = response.url
    	yield data       
