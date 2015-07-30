from scrapy import Spider
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["http://www.thequintessentialgirl.com/"]
    start_urls = ["http://www.thequintessentialgirl.com/9-one-pot-wonders/"]

    def parse(self, response):
    	things = Selector(response).xpath("/html/body/section/section/main/section")
    
        for thing in things:
        	item = CraigslistSampleItem()
        	item['title'] = thing.xpath('//*[@id="post-853"]/header/h1/a/text()').extract()[0]
        	item['post'] = thing.xpath('//*[@id="post-853"]/div/p/text()').extract()[0]
        	
        	yield item
        
        
        
        
        
        
        #hxs = HtmlXPathSelector(response)
        #titles = hxs.Xpath("/html/body/section/section/main/section")
        #for titles in titles:
         #   title = titles.response.selector.xpath("header/h1/a/text()").extract()
          #  post = titles.response.selector.xpath("div/p/text()").extract()
           # print title, post