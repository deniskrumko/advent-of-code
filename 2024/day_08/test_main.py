import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 14


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 252


def test_function_2():
    assert function_2(input_data) == 34


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 839
