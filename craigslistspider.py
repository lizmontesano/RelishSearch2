#this isn't working right now!

import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy

class craigslistspider(scrapy.Spider):
    name = 'craigslist_spider'
    start_urls = ['https://newyork.craigslist.org/search/fua?query=chrome%20chair#search=1~gallery~0~0']

    def parse(self, response):
        print(response.body)
        listings = response.css('li.cl-static-search-result')
        print("listings is..")
        print(listings)

        for listing in listings:
            title = listing.css('div.title::text').get()
            price = listing.css('div.price::text').get()
            #shipping = listing.css('span.s-item__shipping::text').get()
            #returns = listing.css('span.s-item__free-returns::text').get()
            #image_url = listing.css('div.gallery-card img::attr(src)').get()
            image_url = listing.xpath('/html/body/div[1]/main/div/div[5]/ol/li[1]/div/div[1]/div[1]/a/img/@src').get()
            #listing_url =listing.css('').get()
            print(title)
            print(price)
            #print(shipping)
            #print(returns)
            print(image_url)

            yield {
                'title': title.strip() if title else 'N/A title',
                'price': price.strip() if price else 'N/A price',
                #'shipping': shipping.strip() if shipping else 'Free local pickup',
                #'returns': returns.strip() if returns else 'N/A returns',
                'image_url': image_url if image_url else 'N/A image'
            }