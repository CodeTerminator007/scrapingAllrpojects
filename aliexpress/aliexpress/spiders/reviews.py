import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.aliexpress.com/store/feedback-score/3741017.html?spm=a2g0o.detail.1000061.6.636b146crnIeYR',
            wait_time=5,
            callback=self.parse,
        )
        
    def parse(self, response):
        comment = response.xpath('//table[@class="rating-table widthfixed"]/tbody/tr')
        print(comment)
        for res in comment:
            ccc = res.xpath('.//td[3]/div[@class="feedback"]/span/text()').get()
            if ccc:
                yield {
                'COmment' :ccc
                }
