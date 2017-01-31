from os import environ

from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest


class SearchSpider(InitSpider):
    name = 'search'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'

    def __init__(self, *args, **kwargs):
        try:
            self.username = kwargs.pop('username', environ['SPIDER_USERNAME'])
            self.password = kwargs.pop('password', environ['SPIDER_PASSWORD'])
        except KeyError:
            self.logger.error('Both username and password need to be specified '
                              'by -a option or SPIDER_<PARAM> environment var')

        query = kwargs.pop('query', 'Mateusz+Moneta')
        self.start_urls = [
            'https://www.linkedin.com/vsearch/f?type=people&keywords=%s' % query
        ]

        super().__init__(*args, **kwargs)

    def init_request(self):
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        return FormRequest.from_response(
            response, callback=self.check_login_response,
            formdata={'session_key': self.username,
                      'session_password': self.password})

    def parse(self, response):
        for search_result in response.css('li.mod.result.people'):
            *first_name, last_name = search_result.css('b::text').extract()
            yield {
                'first_name': ' '.join(first_name),
                'last_name': last_name,
            }

    def check_login_response(self, response):
        if b'Sign Out' in response.body:
            self.logger.debug("Successfully logged in. Let's start crawling!")
            return self.initialized()

        self.logger.error('Login failed!')
