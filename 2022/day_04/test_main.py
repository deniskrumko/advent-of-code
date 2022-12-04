import pytest

from .main import (
    INPUT_FILE,
    count_fully_overlapping_pairs,
    count_partially_overlapping_pairs,
)

input_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_count_fully_overlapping_pairs():
    assert count_fully_overlapping_pairs(input_data) == 2


def test_count_fully_overlapping_pairs_from_file(file_input_data):
    assert count_fully_overlapping_pairs(file_input_data) == 464


def test_count_partially_overlapping_pairs():
    assert count_partially_overlapping_pairs(input_data) == 4


def test_count_partially_overlapping_pairs_from_file(file_input_data):
    assert count_partially_overlapping_pairs(file_input_data) == 770
