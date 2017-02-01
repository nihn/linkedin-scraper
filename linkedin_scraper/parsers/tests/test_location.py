from pytest import fixture

from linkedin_scraper.parsers import LocationParser


@fixture()
def location_parser():
    return LocationParser()


def test_normal_location(location_parser):
    assert ('Warszawa', 'Polska') == location_parser.parse(
        'Warszawa, woj. mazowieckie, Polska')


def test_location_contains_only_city_and_country(location_parser):
    assert ('Warszawa', 'Polska') == location_parser.parse('Warszawa, Polska')
