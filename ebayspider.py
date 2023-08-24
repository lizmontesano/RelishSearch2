import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy

class eBaySpider(scrapy.Spider):
    name = 'ebay_spider'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1312&_nkw=chrome+chair&_sacat=0&LH_TitleDesc=0&_odkw=chrome+chair&_osacat=0']

    custom_settings = {
        'FEEDS': { 'data.jsonl': { 'format': 'jsonlines',}}
    }

    def parse(self, response):
        listings = response.css('div#srp-river-main ul.srp-results li.s-item')
        
        for listing in listings:
            title = listing.css('div.s-item__title span::text').get()
            price = listing.css('span.s-item__price::text').get()
            delivery = listing.css('span.s-item__shipping::text').get()
            returns = listing.css('span.s-item__free-returns::text').get()
            image_url = listing.css('div.s-item__image-wrapper img::attr(src)').get()
            listing_url = listing.css('div.s-item__image a::attr(href)').get()
            source = 'eBay'

            yield {
                'title': title.strip() if title else 'N/A title',
                'price': price.strip() if price else 'N/A price',
                'delivery': delivery.strip() if delivery else 'Free local pickup. Check listing for details.',
                'returns': returns.strip() if returns else 'N/A returns',
                'image_url': image_url if image_url else 'N/A image',
                'listing_url': listing_url.strip() if listing_url else 'N/A url',
                'source': source
            }