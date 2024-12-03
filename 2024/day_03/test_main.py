import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip('\n')

input_data_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 161


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 182619815


def test_function_2():
    assert function_2(input_data_2) == 48


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 80747545
