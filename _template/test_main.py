import pytest

from .main import function

input_data = []


@pytest.fixture
def file_input_data():
    with open('2021/day_XX/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def test_function_1():
    assert function(input_data)


def test_function_1_from_file(file_input_data):
    assert function(file_input_data)


def test_function_2():
    assert function(input_data)


def test_function_2_from_file(file_input_data):
    assert function(file_input_data)
