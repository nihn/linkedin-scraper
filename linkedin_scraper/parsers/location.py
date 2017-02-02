from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class LocationParser(BaseParser):
    def parse(self, item: str) -> Tuple[str, str]:
        """
        Parse LinkedIn location string into city and country. Return
        empty string for missing ones.
        :param item: location string
        :return: city, country
        """
        try:
            city, *_, country = item.split(',')
        except ValueError:
            return '', item
        return city.strip(), country.strip()
