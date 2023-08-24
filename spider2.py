import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy

class spider2(scrapy.Spider):
    name = 'Ebay'
    #this is the URL I get when I search "chrome chair"
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313&_nkw=chrome+chair&_sacat=0']

    def parse(self, response):
        #get the wrapper that includes all the listings 
        items = response.css('div.s-item__wrapper').getall()

        for item in items:
            header = item.css('div.s-item__title span::text').get()
            print(header)
            price = item.css('div.s-item__detail span.s-item__price::text').get()
            price(price)

            yield {
                'header': header.strip() if header else None,
                'price': price.strip() if price else None
            }