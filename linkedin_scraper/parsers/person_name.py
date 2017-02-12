import re
from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class PersonNameParser(BaseParser):
    forbidden_chars_pattern = re.compile(r'[^\w^\s]', re.UNICODE)

    def __init__(self):
        self.names_list = self.get_lines_from_datafile('names_list.txt')
        self.surnames_list = self.get_lines_from_datafile('surnames_list.txt')
        self.surname_affixes_list = self.get_lines_from_datafile(
            'surname_affixes_list.txt')

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
        Categorize names into four groups: first_names, surnames, affixes and
        unknown.
        """
        first_names, surnames, affixes, unknown = [], [], [], []

        for name in names:
            lower_name = name.lower()

            if lower_name in self.surname_affixes_list:
                affixes.append(name)
            elif lower_name in self.names_list:
                first_names.append(name)
            elif lower_name in self.surnames_list:
                surnames.append(name)
            else:
                unknown.append(name)

        return first_names, surnames, affixes, unknown

    def _parse(self, item: str) -> Tuple[str, str]:
        if not item:
            return [''], ''

        # Names listed by LinkedIn do not have ',' included
        item = item.split(',')[0]
        # Remove all unwanted chars
        item = self.forbidden_chars_pattern.sub('', item)

        names = [name.capitalize() for name in item.split()]
        first_names, surnames, affixes, unknown = self._categorize_items(names)

        if len(surnames) == 1 and first_names:
            # We found surname and first_name(s)
            return first_names, surnames[0]

        if affixes:
            affix_index_l = names.index(affixes[0])
            affix_index_r = names.index(affixes[-1])

            if names[affix_index_r + 1:] and names[:affix_index_l]:
                # Noble kind of surname, e.g. <first name> von der <surname>
                return names[:affix_index_l], ' '.join(names[affix_index_l:])

        if first_names and not surnames and len(unknown) == 1:
            # We did't find surname but everything except for one item was
            # recognized as first name
            return first_names, unknown[0]

        # Everything above failed, use naive approach:
        # assume that last item is surname
        return names[:-1], names[-1]
