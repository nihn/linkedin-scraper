from os import getenv

BOT_NAME = 'linkedin_scraper'
SPIDER_MODULES = ['linkedin_scraper.spiders']
NEWSPIDER_MODULE = 'linkedin_scraper.spiders'
COMMANDS_MODULE = 'linkedin_scraper.commands'

USER_AGENT = 'linkedin_scraper (+https://www.github.com/nihn/linkedin_scraper)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Splash settings taken from https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/
SPLASH_URL = getenv('SPLASH_ADDR', 'http://localhost:8050/')

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.'
    'HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

#######################################
