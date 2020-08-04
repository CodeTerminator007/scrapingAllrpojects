import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    
    
    script = '''
    function main(splash, args) 
      splash.private_mode_enabled = false
      splash:set_custom_headers(headers)
      assert(splash:go(args.url))
      assert(splash:wait(1))
      box = assert(splash:select_all(".filterPanelItem___2z5Gb"))
      box[6]:mouse_click()
      splash:set_viewport_full()
      assert(splash:wait(2))
      
      return {
        html = splash:html(),
        }
    end
    '''
    def start_requests(self):
        yield SplashRequest(url = "https://www.livecoin.net/en" , callback = self.parse , endpoint ="execute" , args={
            'lua_source' : self.script
            })
    def parse(self, response):
        print(response.body)
