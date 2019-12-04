# -*- coding: utf-8 -*-
import scrapy


class TechehubSpider(scrapy.Spider):
    name = 'techehub'
    allowed_domains = ['wwww.techehub.com']
    start_urls = ['http://wwww.techehub.com/']

    def parse(self, response):
        pass
