import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 10605


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 66124


@pytest.mark.skip('Not ready')
def test_function_2():
    assert function_2(input_data, 10000) == 2713310158


@pytest.mark.skip('Not ready')
def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data)
