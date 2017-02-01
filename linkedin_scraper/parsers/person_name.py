from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class PersonNameParser(BaseParser):
    def __init__(self):
        self.names_list = self.get_lines_from_datafile('names_list.txt')
        self.surnames_list = self.get_lines_from_datafile('surnames_list.txt')

    def parse(self, item: str) -> Tuple[str, str]:
        """
        Parse string with person name into two pieces:
        <first, second, ... name> and <last name>
        :param item: name string
        :return: first...n name, last name
        """
        if not item:
            return '', ''
        names = item.split()
        return ' '.join(names[:-1]), names[-1]
