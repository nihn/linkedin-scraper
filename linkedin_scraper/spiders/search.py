import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['linkedin.com']
    start_urls = ['http://linkedin.com/']

    def parse(self, response):
        pass
