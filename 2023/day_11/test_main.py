import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

@pytest.mark.parametrize('expansion_size, expected', (
    (2, 374),
    (10, 1030),
    (100, 8410),
))
def test_function_1(expansion_size, expected):
    assert function_1(input_data, expansion_size) == expected


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 10033566


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 560822911938
