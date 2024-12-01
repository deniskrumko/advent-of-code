import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 11


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 2113135


def test_function_2():
    assert function_2(input_data) == 31


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 19097157
