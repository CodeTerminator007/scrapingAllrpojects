from selenium import webdriver
from shutil import which
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By    # For selecting html code
import time


chrome_options = Options()
chrome_options.add_argument('--headless')       #to make  it headless
chrome_path = which ("chromedriver")
driver = webdriver.Chrome(executable_path= chrome_path  )
driver.get("https://www.pickstar.com.au/our-stars")
time.sleep(3)
for i in range(1,2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 2000);")
    time.sleep(10)
html = driver.page_source
response_obj = Selector(text=html)
bodys = response_obj.xpath('//div[@class="col-sm-6 col-md-4 col-lg-3"]')
for row in bodys:
    link = row.xpath('.//div/div/div[1]/a/@href').get()
    print(link)
driver.close()
