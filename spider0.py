import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

import scrapy

class spider1(scrapy.Spider):
    name = 'Wikipedia'
    start_urls = ['https://www.imdb.com/chart/boxoffice/']

    def parse(self, response):
        print('line 11')
        for e in response.css('div#boxoffice>table>tbody>tr'):
            print('line 13')
            print(e)
            print ('line 15')
            yield {
                'title': ''.join(e.css('td.titleColumn>a::text').extract()).strip(),
                'weekend': ''.join(e.css('td.ratingColumn')[0].css('::text').extract()).strip(),
                'gross': ''.join(e.css('td.ratingColumn')[1].css('span.secondaryInfo::text').extract()).strip(),
                'weeks': ''.join(e.css('td.weeksColumn::text').extract()).strip(),
                'image': e.css('td.posterColumn img::attr(src)').extract_first(),
            }
            print ('line 23)')