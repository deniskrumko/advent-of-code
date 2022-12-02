import pytest

from .main import (
    INPUT_FILE,
    get_total_score,
    get_total_score_with_new_rules,
)

input_data = """
A Y
B X
C Z
""".strip()


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_get_total_score():
    assert get_total_score(input_data) == 15


def test_get_total_score_from_file(file_input_data):
    assert get_total_score(file_input_data) == 14264


def test_get_total_score_with_new_rules():
    assert get_total_score_with_new_rules(input_data) == 12


def test_get_total_score_with_new_rules_from_file(file_input_data):
    assert get_total_score_with_new_rules(file_input_data) == 12382
