import scrapy
from selenium import webdriver
from shutil import which
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By    # For selecting html code
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

chrome_options = Options()
chrome_options.add_argument('--headless')       #to make  it headless
chrome_path = which ("chromedriver")
driver = webdriver.Chrome(executable_path= chrome_path  )
driver.get("https://www.pickstar.com.au/our-stars")
time.sleep(3)
for i in range(1,3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 2000);")
    time.sleep(10)
html = driver.page_source
response_obj = Selector(text=html)
bodys = response_obj.xpath('//div[@class="col-sm-6 col-md-4 col-lg-3"]')


class Test1Spider(CrawlSpider):
    name = 'test1'
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="col-sm-6 col-md-4 col-lg-3"]/div/div/div[1]/a/@href'), callback='parse_item', follow=True),
        )

    def parse_item(self, response):
        name = response.xpath('//h2[@itemprop="name"]/text()')
        print(name)

driver.close()