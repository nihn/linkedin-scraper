from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class PersonNameParser(BaseParser):
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
