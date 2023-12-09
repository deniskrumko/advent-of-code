import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
    get_extrapolated_value,
)

input_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 114


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 1641934234


def test_function_2():
    assert function_2(input_data) == 2


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 975


@pytest.mark.parametrize('value, expected, left', (
    ('0 3 6 9 12 15', 18, False),
    ('1 3 6 10 15 21', 28, False),
    ('10 13 16 21 30 45', 68, False),
    ('0 3 6 9 12 15', -3, True),
    ('1 3 6 10 15 21', 0, True),
    ('10 13 16 21 30 45', 5, True),
))
def test_get_extrapolated_value(value, expected, left):
    value = [int(v) for v in value.split()]
    assert get_extrapolated_value(value, left=left) == expected
