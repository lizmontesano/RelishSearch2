import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy

class spider1(scrapy.Spider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Electric_battery']

    def parse(self, response):
        #get the header of the wikipedia page
        print(response.css('h1#firstHeading span.mw-page-title-main::text').get())

class spider2(scrapy.Spider):
    name = 'Ebay'
    #this is the URL I get when I search "chrome chair"
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313&_nkw=chrome+chair&_sacat=0']

    def parse(self, response):
        #get the headers of the first page of listings
        print(response.css('span.s-item__title::text').get())


