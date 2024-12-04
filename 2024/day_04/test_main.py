import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip('\n')

input_data_2 = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 18


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 2468


def test_function_2():
    assert function_2(input_data_2) == 9


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 1864
