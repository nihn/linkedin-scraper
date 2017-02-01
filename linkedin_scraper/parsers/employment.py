from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class EmploymentParser(BaseParser):
    def parse(self, item: str) -> Tuple[str, str]:
        """
        Parse LinkedIn employment string into position and company.
        :param item: employment string
        :return: position, company
        """
        if ' at ' in item:
            # Easy case, standard LinkedIn format <position> at <company>
            return tuple(item.split(' at ', maxsplit=1))

        # We don't know which is which so return whole item as a position
        return item, ''
