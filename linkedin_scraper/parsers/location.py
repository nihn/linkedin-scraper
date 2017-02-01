from typing import Tuple

from linkedin_scraper.parsers.base import BaseParser


class LocationParser(BaseParser):
    def parse(self, item: str) -> Tuple[str, str]:
        """
        Parse LinkedIn location string into city and country.
        :param item: location string
        :return: city, country
        """
        city, *_, country = item.split(',')
        return city.strip(), country.strip()
