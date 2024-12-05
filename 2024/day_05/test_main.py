import pytest

from .main import (
    INPUT_FILE,
    Page,
    Puzzle,
    function_1,
    function_2,
)

input_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 143


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 4281


@pytest.mark.parametrize('value, expected', (
    ('75,97,47,61,53', '97,75,47,61,53'),
    ('61,13,29', '61,29,13'),
    ('97,13,75,29,47', '97,75,47,29,13'),
))
def test_fix_page(value, expected):
    puzzle = Puzzle.parse(input_data)
    assert puzzle.fix_page(Page.parse(value)) == Page.parse(expected)


def test_function_2():
    assert function_2(input_data) == 123


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 5466
