from linkedin_scraper.parsers import BaseParser


class PersonNameParser(BaseParser):
    def parse(self, item):
        """
        Parse string with person name into two pieces:
        <first, second, ... name> and <last name>
        :param item: name string
        :type: str
        :return: first...n name, last name
        :rtype: tuple(str, str)
        """
        if not item:
            return '', ''
        names = item.split()
        return ' '.join(names[:-1]), names[-1]
