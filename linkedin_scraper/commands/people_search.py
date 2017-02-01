from getpass import getpass

from scrapy.commands.crawl import Command as BaseCommand


def sanitize_query(query):
    return query.replace(' ', '+')


class Command(BaseCommand):
    def short_desc(self):
        return "Scrap people from LinkedIn"

    def syntax(self):
        return "[options] <query>"

    def add_options(self, parser):
        super().add_options(parser)

        parser.add_option('-u', '--username', help='Name of LinkedIn account')
        parser.add_option('-p', '--password',
                          help='Password for LinkedIn account')

    def process_options(self, args, opts):
        super().process_options(args, opts)

        opts.output = opts.output or 'results.csv'

        people_search_options = {
            'query': sanitize_query(args[0]),
            'username': opts.username or input(
                'Please provide your LinkedIn username: '),
            'password': opts.password or getpass(
                'Please provide password for your LinkedIn account: ')
        }
        opts.spargs.update(people_search_options)

    def run(self, args, opts):
        # Run people_search spider
        args = ['people_search']
        super().run(args, opts)
