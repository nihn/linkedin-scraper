from pytest import fixture

from linkedin_scraper.parsers import EmploymentParser


@fixture()
def employment_parser():
    return EmploymentParser()


def test_regular_linkedin_format(employment_parser):
    assert ('Python Developer', 'Foo Software') == employment_parser.parse(
        'Python Developer at Foo Software')


def test_unknown_format(employment_parser):
    assert ('Python Developer', '') == employment_parser.parse(
        'Python Developer')


def test_multiple_at_in_employment_str(employment_parser):
    assert ('Developer', 'Foo at Bar') == employment_parser.parse(
        'Developer at Foo at Bar')
