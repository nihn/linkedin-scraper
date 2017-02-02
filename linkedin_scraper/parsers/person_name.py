import re
from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class PersonNameParser(BaseParser):
    forbidden_chars_pattern = re.compile(r'[^\w^\s]', re.UNICODE)

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
        first_names, surname = self._parse(item)
        return ' '.join(first_names), surname

    def _categorize_items(self, names):
        """
        Categorize names into three groups: first_names, surnames, affixes and
        unknown.
        """
        first_names, surnames, unknown = [], [], []

        for name in names:
            lower_name = name.lower()

            if lower_name in self.names_list:
                first_names.append(name)
            elif lower_name in self.surnames_list:
                surnames.append(name)
            else:
                unknown.append(name)

        return first_names, surnames, unknown

    def _parse(self, item: str) -> Tuple[str, str]:
        if not item:
            return [''], ''

        # Remove all unwanted items
        item = self.forbidden_chars_pattern.sub('', item)

        names = [name.capitalize() for name in item.split()]
        first_names, surnames, unknown = self._categorize_items(names)

        if len(surnames) == 1 and first_names:
            # We found surname and first_name(s)
            return first_names, surnames[0]

        if first_names and not surnames and len(unknown) == 1:
            # We did't find surname but everything except one item was
            # recognized as first name
            return first_names, unknown[0]

        # Everything else failed, assume that last item is surname
        return names[:-1], names[-1]
