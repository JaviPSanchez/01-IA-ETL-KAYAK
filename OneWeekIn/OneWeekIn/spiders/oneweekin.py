import scrapy

class OneWeekSpider(scrapy.Spider):

    name = "oneweekin"

    def start_requests( self ):
        urls = ['https://one-week-in.com/35-cities-to-visit-in-france/']
        for url in urls:
            yield url

    def parse(self, response):
        results = response.css('div.entry-content')
        for p in results:
            yield {
                'city': p.css('h2 ::text').getall(),
                'text': p.css('::text').getall()
            }
            

        

        