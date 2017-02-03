from pytest import fixture

from linkedin_scraper.parsers import EmploymentParser


@fixture()
def employment_parser():
    parser = EmploymentParser()
    parser.professions_list = []
    return parser


def test_regular_linkedin_format(employment_parser):
    assert ('Python Developer', 'Foo Software') == employment_parser.parse(
        'Python Developer at Foo Software')


def test_unknown_format(employment_parser):
    assert ('Python Developer', '') == employment_parser.parse(
        'Python Developer')


def test_multiple_at_in_employment_str(employment_parser):
    assert ('Developer', 'Foo at Bar') == employment_parser.parse(
        'Developer at Foo at Bar')


def test_position_found_in_profession_list(employment_parser):
    employment_parser.professions_list = {'developer'}

    assert ('Senior Python Developer', 'Foo Software') == \
        employment_parser.parse('Senior Python Developer, Foo Software')


def test_position_found_in_profession_list_without_company(employment_parser):
    employment_parser.professions_list = {'developer'}

    assert ('Senior Python Developer', '') == employment_parser.parse(
        'Senior Python Developer')
