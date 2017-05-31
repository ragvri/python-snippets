import scrapy
from scrapy.crawler import CrawlerProcess
import logging

logging.getLogger('scrapy').propagate = False  # disables the log output


class MySpider(scrapy.Spider):
    name = 'test'
    start_urls = ["http://quotes.toscrape.com/page/1"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            print(quote.css('span.text ::text').extract_first())
        next_page = response.css('li.next a::attr(href)').extract_first()  # go to the next page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            scrapy.Request(next_page, self.parse)


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

process.crawl(MySpider)
process.start()
# the script will block here until the crawling is finished
