import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_1a,
    function_2,
    function_2a,
)

input_data = """
Time:      7  15   30
Distance:  9  40  200
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == function_1a(input_data) == 288


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == function_1a(file_input_data) == 1731600


def test_function_2():
    assert function_2(input_data) == function_2a(input_data) == 71503


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == function_2a(file_input_data) == 40087680
