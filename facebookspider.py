#this isn't working right now!

import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy
from scrapy_splash import SplashRequest

class FacebookSpider(scrapy.Spider):
    name = 'facebook_spider'
    start_urls = ['https://www.facebook.com/marketplace/nyc/search/?query=chrome%20chair&exact=false']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})
    
    custom_settings = {
        'FEEDS': { 'data.jsonl': { 'format': 'jsonlines',}}
    }

    def parse(self, response):
        listings = response.css('div.x9f619.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xs83m0k.x1e558r4.x150jy0e.x1iorvi4.xjkvuk6.xnpuxes.x291uyu.x1uepa24')
        print(listings)

        for listing in listings:
            title = listing.css('span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6::text').get()
            print(title)
            price = listing.css('div.x78zum5.x1q0g3np.x1iorvi4.x4uap5.xjkvuk6.xkhd6sd span::text').get()
            print(price)
            delivery_loc = listing.css('span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft::text').get()
            delivery = f"Free local pick up from {delivery_loc}"
            print(delivery) 
            returns = 'No returns'
            print(returns)
            image_url = listing.css('div.x9f619 img::attr(src)').get()
            print(image_url) 
            url = listing.css('a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.x1lku1pv::attr(href)').get()
            listing_url = f"https://www.facebook.com{url}"
            print(listing_url)
            source = 'Facebook Marketplace'

            yield {
                'title': title.strip() if title else 'N/A title',
                'price': price.strip() if price else 'N/A price',
                'delivery': delivery.strip() if delivery else 'N/A shipping',
                'returns': returns.strip() if returns else 'N/A returns',
                'image_url': image_url if image_url else 'N/A image',
                'listing_url': listing_url.strip() if listing_url else 'N/A url',
                'source': source
            }


#class facebookSpider(scrapy.Spider):
    #name = 'facebook_spider'
    #start_urls = ['https://www.facebook.com/marketplace/nyc/search?query=chrome%20chair']

    #def parse(self, response):
        
        #listings = response.css('div#mount_0_0_Xs')
        #print(listings)

        #for listing in listings:
            #title = listing.css('div.x9f619.x78zum5.xdt5ytf.x1qughib.x1rdy4ex.xz9dl7a.xsag5q8.xh8yej3.xp0eagm.x1nrcals div.x1gslohp.xkh6y0r span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.xlh3980.xvmahel.x1n0sxbx.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x3x7a5m.x1lkfr7t.x1lbecb7.x1s688f.xzsf02u::text').get()
            #price = listing.css('span.x193iq5w::text').get()
            #shipping = listing.css('INSERT').get()
            #returns = listing.css('INSERT').get()
            #image_url = listing.css('div.x9f619 img::attr(src)').get()
            #print(title)
            #print(price)
            #print(shipping)
            #print(returns)
            #print(image_url)

            #yield {
                #'title': title.strip() if title else 'N/A title',
                #'price': price.strip() if price else 'N/A price',
                #'shipping': shipping.strip() if shipping else 'Free local pickup',
                #'returns': returns.strip() if returns else 'N/A returns',
                #'image_url': image_url if image_url else 'N/A image'
            #}