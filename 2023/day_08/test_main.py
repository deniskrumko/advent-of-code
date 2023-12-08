import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip('\n')

input_data_2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 6


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 19637


def test_function_2():
    assert function_2(input_data_2) == 6


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 8811050362409
