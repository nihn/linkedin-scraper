import logging
from os import path

import linkedin_scraper

logger = logging.getLogger(__name__)


class BaseParser:
    @staticmethod
    def get_data_dir():
        return path.abspath(path.join(linkedin_scraper.__file__,
                            '../..', 'data'))

    @staticmethod
    def normalize_lines(lines):
        return set(line.lower().strip() for line in lines)

    def get_lines_from_datafile(self, name: str) -> set:
        """
        Get and normalize lines from datafile.
        :param name: name of the file in package data directory
        """
        try:
            with open(path.join(self.get_data_dir(), name)) as f:
                return self.normalize_lines(f)
        except FileNotFoundError:
            logger.error('%s not found', name)
            return set()

    def parse(self, item):
        raise NotImplemented()
