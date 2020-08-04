import scrapy
from scrapy_splash import SplashRequest

class BotSpider(scrapy.Spider):
    name = 'bot'
    allowed_domains = ['www.dabemetv.com.br']
    
    
    script = ''' 
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            for i = 10,1,-1 do 
            
                box =  assert(splash:select("#PDI_answer48967433"))
                box:mouse_click()
                vote = assert(splash:select("#pd-vote-button10498392"))
                vote:mouse_click()
                assert(splash:wait(2))
                back = assert(splash:select(".pds-return-poll"))
                back:mouse_click()
            end
            return {
             png = splash:png(),
            }
        end
    '''
    def start_requests(self):
        
        yield SplashRequest(url="https://www.dabemetv.com.br/2020/07/bestsong.html", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script ,  'timeout': 3600
        })
                
    def parse(self, response):
        print (response.body)
