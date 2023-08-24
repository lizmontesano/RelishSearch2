import json

import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy

class remixSpider(scrapy.Spider):
    name = 'remix_spider'
    start_urls = ['https://www.remixmarketnyc.com/search/chrome+chair/']
    
    custom_settings = {
        'FEEDS': { 'data.jsonl': { 'format': 'jsonlines',}}
    }

    def parse(self, response):

        listings = response.css('div.product.col-xs-6.col-sm-3.col-md-3')
 
        for listing in listings:
            title = listing.css('div.info a.title::text').get()
            price = listing.css('div.info div.left::text').get()
            image_url = listing.css('div.image-wrap img::attr(src)').get()
            listing_url = listing.css('.product a.title::attr(href)').getall()
            source = 'Remix Market'

            yield {
                'title': title.strip() if title else 'N/A title',
                'price': price.strip() if price else 'N/A price',
                'delivery': 'Free local pickup from Long Island City, NY',
                'returns': 'Final sale',
                'image_url': image_url if image_url else 'N/A image',
                'listing_url': listing_url.strip() if image_url else 'N/A url',
                'source': source
            }