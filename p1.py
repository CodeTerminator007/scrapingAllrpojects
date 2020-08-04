import scrapy


class P1Spider(scrapy.Spider):
    name = 'p1'
    allowed_domains = ['www.pickstar.com.au/our-stars']
    start_urls = ['http://www.pickstar.com.au/our-stars/']

    def parse(self, response):
        pass
