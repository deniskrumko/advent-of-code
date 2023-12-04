import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 13


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 20117


def test_function_2():
    assert function_2(input_data) == 30


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 13768818
