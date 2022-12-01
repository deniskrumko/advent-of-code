import pytest

from .main import (
    max_calories,
    top_calories,
)

input_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip().split('\n')


@pytest.fixture
def file_input_data():
    with open('2022/day_01/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def test_function_1():
    assert max_calories(input_data) == 24000


def test_function_1_from_file(file_input_data):
    assert max_calories(file_input_data) == 71506


def test_function_2():
    assert top_calories(input_data) == 45000


def test_function_2_from_file(file_input_data):
    assert top_calories(file_input_data) == 209603
