import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 3749


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 20665830408335


def test_function_2():
    assert function_2(input_data) == 11387


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 354060705047464
