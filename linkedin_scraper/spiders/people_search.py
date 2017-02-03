from os import environ

from scrapy_splash import SplashRequest
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest

from linkedin_scraper.parsers import (
    EmploymentParser,
    LocationParser,
    PersonNameParser,
)


class PeopleSearchSpider(InitSpider):
    name = 'people_search'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'

    name_parser = PersonNameParser()
    employment_parser = EmploymentParser()
    location_parser = LocationParser()

    def __init__(self, *args, **kwargs):
        try:
            self.username = kwargs.pop('username')
            self.password = kwargs.pop('password')
            query = kwargs.pop('query')
        except KeyError:
            raise Exception('Missing option, please use `scrapy people_search '
                            'cmd to use this spider')

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
            names = search_result.css('a.title.main-headline').xpath(
                'string(.)').extract_first()
            employment = search_result.css('div.description').xpath(
                'string(.)').extract_first()
            location = search_result.css('bdi::text').extract_first()

            first_name, last_name = self.name_parser.parse(names)
            position, company = self.employment_parser.parse(employment)
            city, country = self.location_parser.parse(location)

            yield {
                'first_name': first_name,
                'last_name': last_name,
                'position': position,
                'company': company,
                'city': city,
                'country': country,
            }

    def check_login_response(self, response):
        if b'Sign Out' in response.body:
            self.logger.info("Successfully logged in. Let's start crawling!")
            return self.initialized()

        error_msg = response.css('span.error::text').extract_first()

        if 'not the right password' in error_msg:
            self.logger.error('Invalid password')
        elif "we don't recognize that email" in error_msg:
            self.logger.error('Invalid email')
        else:
            self.logger.error('Unknown error, cannot log in')

        self.logger.debug('Error msg for server: %s', error_msg)

    def make_requests_from_url(self, url):
        # Do SplashRequest instead of regular one to be able to evaluate
        # JavaScript responsible for dynamic page generation.
        return SplashRequest(url)
