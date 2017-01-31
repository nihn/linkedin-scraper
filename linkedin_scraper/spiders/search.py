import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['linkedin.com']
    start_urls = [
        'https://www.linkedin.com/vsearch/f?type=people&keywords=MateuszMoneta']

    def parse(self, response):
        for search_result in response.css('li.mod.result.people'):
            *first_name, last_name = search_result.css('b::text').extract()
            yield {
                'first_name': ' '.join(first_name),
                'last_name': last_name,
            }
