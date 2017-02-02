from pytest import fixture

from linkedin_scraper.parsers import LocationParser


@fixture()
def location_parser():
    return LocationParser()


def test_normal_location(location_parser):
    assert ('Warszawa', 'Poland') == location_parser.parse(
        'Warszawa, woj. mazowieckie, Poland')


def test_location_contains_only_city_and_country(location_parser):
    assert ('Warszawa', 'Poland') == location_parser.parse('Warszawa, Poland')


def test_location_only_country(location_parser):
    assert ('', 'Poland') == location_parser.parse('Poland')


def test_location_empty(location_parser):
    assert ('', '') == location_parser.parse('')
