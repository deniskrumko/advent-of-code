import pytest

from .main import (
    INPUT_FILE,
    get_score_part_1,
    get_score_part_2,
)

input_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_get_score_part_1():
    assert get_score_part_1(input_data) == 157


def test_get_score_part_1_from_file(file_input_data):
    assert get_score_part_1(file_input_data) == 7990


def test_get_score_part_2():
    assert get_score_part_2(input_data) == 70


def test_get_score_part_2_from_file(file_input_data):
    assert get_score_part_2(file_input_data) == 2602
