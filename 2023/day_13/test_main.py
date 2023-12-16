import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
    parse_data,
)

input_data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 405


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 30705


def test_function_2():
    assert function_2(input_data) == 400


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 44615


def test_methods():
    p1, p2 = parse_data(input_data)

    assert p1.get_ver_reflection(False) == 5
    assert p1.get_hor_reflection(False) == 0

    assert p1.get_ver_reflection(True) == 0
    assert p1.get_hor_reflection(True) == 3

    assert p2.get_ver_reflection(False) == 0
    assert p2.get_hor_reflection(False) == 4

    assert p2.get_ver_reflection(True) == 0
    assert p2.get_hor_reflection(True) == 1
