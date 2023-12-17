import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 46


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 7860


def test_function_2():
    assert function_2(input_data) == 51


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 8331
