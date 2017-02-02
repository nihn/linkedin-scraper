from pytest import fixture

from linkedin_scraper.parsers.person_name import PersonNameParser


@fixture()
def person_name_parser():
    parser = PersonNameParser()
    parser.surnames_list = []
    parser.names_list = []
    return parser


def test_regular_name(person_name_parser):
    assert ('Mateusz', 'Moneta') == person_name_parser.parse('Mateusz Moneta')


def test_one_name(person_name_parser):
    assert ('', 'Moneta') == person_name_parser.parse('Moneta')


def test_first_and_second_name(person_name_parser):
    assert ('Mateusz Marek', 'Moneta') == person_name_parser.parse(
        'Mateusz Marek Moneta')


def test_empty_name(person_name_parser):
    assert ('', '') == person_name_parser.parse('')


def test_detected_one_surname_and_first_name(person_name_parser):
    person_name_parser.names_list = ['john', 'brian']
    person_name_parser.surnames_list = ['smith']

    assert ('John Brian', 'Smith') == person_name_parser.parse(
        'Smith John Brian')


def test_first_names_found_with_one_item_unknown(person_name_parser):
    person_name_parser.names_list = ['john', 'brian']

    assert ('John Brian', 'Smith') == person_name_parser.parse(
        'Smith John Brian')
