import scrapy

class MySpider(scrapy.Spider):
    name = 'arabic_spider'
    start_urls = ['https://ar.wikipedia.org/wiki/%D9%8A%D9%88%D8%B3%D9%81_%D8%A8%D9%86_%D8%AA%D8%A7%D8%B4%D9%81%D9%8A%D9%86']

    def parse(self, response):

        yield  { "Data": response.css('p::text').extract()}