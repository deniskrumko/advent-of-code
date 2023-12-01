import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip('\n')

input_data_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 142


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 53921


def test_function_2():
    assert function_2(input_data_2) == 281


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 54676
