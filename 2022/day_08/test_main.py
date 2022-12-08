import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
30373
25512
65332
33549
35390
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 21


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 1715


def test_function_2():
    assert function_2(input_data) == 8


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 374400
