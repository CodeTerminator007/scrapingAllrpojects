import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class AllstarsurlSpider(scrapy.Spider):
    name = 'Allstarsurl'

    def start_requests(self):
        yield SeleniumRequest(url='https://www.pickstar.com.au/our-stars',
        wait_time=3,
        callback=self.parse) 

    def parse(self, response):
        driver = response.meta['driver']
        for i in range(1,1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 2000);")
            time.sleep(1.5)
        html = driver.page_source
        response_obj = Selector(text=html)
        bodys = response_obj.xpath('//div[@class="col-sm-6 col-md-4 col-lg-3"]')
        for row in bodys:
            link = row.xpath('.//div/div/div[1]/a/@href').get()
            if link:
                time.sleep(4.5)
                yield SeleniumRequest(url=link,wait_time=3,callback=self.scras)      

    def scras(self,response):
        time.sleep(4.5)        
        driver = response.meta['driver']
        pge = driver.page_source        
        response_obj2 = Selector(text=pge)                                     
        yield{
            'Name ': response_obj2.xpath('//h2[@itemprop="name"]/text()').get(),
        }
        

