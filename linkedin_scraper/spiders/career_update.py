import scrapy


class CareerUpdateSpider(scrapy.Spider):
    """
    Helper spider for generating list of English professions.
    """

    name = 'career_update'
    allowed_domains = ['careerplanner.com']
    start_urls = [
        'https://www.careerplanner.com/ListOfCareers.cfm',
    ]

    def parse(self, response):
        for career in response.css('div.centercontentcolumn').xpath(
                './a/text()').extract():
            career = career.split(',')[0]
            for profession in career.split(' and '):
                yield {
                    'career': ' '.join([word.rstrip('s').strip()
                                        for word in profession.split()])
                }
