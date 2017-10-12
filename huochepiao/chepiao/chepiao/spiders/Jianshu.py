
from scrapy.spiders.crawl import CrawlSpider
from scrapy.selector import Selector

class JianShu(CrawlSpider):
     name = 'jianshu'
     start_urls = ['http://www.jianshu.com']
     url = 'http://www.jianshu.com'

     def parse(self, response):
         selector = Selector(response)

         articles = selector.xpath('//ul[@class="article-list thumbnails"]/li')

         for article in articles:
             title = article.xpath('div/h4/a/text()').extract()
             url = article.xpath('div/h4/a/@href').extract()
             author = article.xpath('div/p/a/text()').extract()

             item = {}
             item['title'] = title
             item['url'] = 'http://www.jianshu.com/' + url[0]
             item['author'] = author

             yield item

