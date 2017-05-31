# Spiders are clases that scrappy uses to scrape info from a website

import scrapy


# the spiders should be put in the spiders directory of the project


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # identifies the spider

    def start_requests(self):  # returns an iterable of requests which the spider will crawl from
        urls = [
            "http://quotes.toscrape.com/page/1",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # instead of the function start_requests() just create a variable
    # start_urls = ["http://quotes.toscrape.com/page/1"]

    def parse(self, response):  # method that will be called to handle the response download for each request made
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text ::text').extract_first(),
                'author': quote.css('small.author ::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first() # go to the next page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            scrapy.Request(next_page, self.parse)

            # When we run it, scrapy schedules the scrapy.Request objects returned by start_requests method of the
            # spider. Upon receiving response for each one, it instantiates Response objects and calls parse method,
            # passing the response as an argument

            # to run this crawler, run `scrapy crawl quotes` from the top level directory of the project
