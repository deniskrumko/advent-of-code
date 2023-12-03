import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 4361


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 528819


def test_function_2():
    assert function_2(input_data) == 467835


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 80403602
