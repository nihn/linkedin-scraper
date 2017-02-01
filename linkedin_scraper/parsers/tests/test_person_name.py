from pytest import fixture

from linkedin_scraper.parsers.person_name import PersonNameParser


@fixture()
def person_name_parser():
    return PersonNameParser()


def test_regular_name(person_name_parser):
    assert ('Mateusz', 'Moneta') == person_name_parser.parse('Mateusz Moneta')


def test_one_name(person_name_parser):
    assert ('', 'Moneta') == person_name_parser.parse('Moneta')


def test_first_and_second_name(person_name_parser):
    assert ('Mateusz Marek', 'Moneta') == person_name_parser.parse(
        'Mateusz Marek Moneta')


def test_empty_name(person_name_parser):
    assert ('', '') == person_name_parser.parse('')
