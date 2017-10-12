#!/usr/bin/env python
# -*- coding: utf-8 -*-



from scrapy.spiders.crawl import CrawlSpider
from scrapy.selector import Selector
# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CUW&purpose_codes=ADULT"


class Ticket(CrawlSpider):
     name = 'ticket'

     # url = 'http://www.jianshu.com'
     url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CUW&purpose_codes=ADULT"
     start_urls = [url]

     def parse(self, response):
          selector = Selector(response)
          print selector.response.text

