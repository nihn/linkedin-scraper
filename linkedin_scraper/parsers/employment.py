from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class EmploymentParser(BaseParser):
    def __init__(self):
        self.professions_list = self.get_lines_from_datafile(
            'professions_list.txt')

    def parse(self, item: str) -> Tuple[str, str]:
        """
        Parse LinkedIn employment string into position and company.
        :param item: employment string
        :return: position, company
        """
        if ' at ' in item:
            # Simplest case, standard LinkedIn format <position> at <company>
            return tuple(item.split(' at ', maxsplit=1))

        words = item.split()

        for index, word in enumerate(reversed(item.split())):
            normalized_word = word.strip(',.-').lower()

            if normalized_word in self.professions_list:
                founded_profession_index = len(words) - index
                break
        else:
            # We don't know which is which so return whole string as a position
            return item, ''

        # We found profession name in employment string, everything
        # after it is company name
        return (' '.join(words[:founded_profession_index]).rstrip(',.- '),
                ' '.join(words[founded_profession_index:]).lstrip(',.- '))

