# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
from ..items import CourseItem

class ExpertzlabSpider(scrapy.Spider):
    name = 'expertzlab'
    allowed_domains = ['http://www.expertzlab.com']
    start_urls = ['http://www.expertzlab.com/courses.html']

    def parse(self, response):
        #print (response.text)
        soup = bs(response.text, 'html5lib')
        courses = soup.findAll('div', attrs={'class': 'course'})

        for course in courses:
            item = CourseItem()
            item['title'] = course.h4.text
            item['desc'] = course.p.text
            item['duration']  = course.ul.li.text


            yield item
