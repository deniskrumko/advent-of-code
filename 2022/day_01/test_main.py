import pytest

from .main import (
    INPUT_FILE,
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
""".strip()


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


def test_max_calories():
    assert max_calories(input_data) == 24000


def test_max_calories_from_file(file_input_data):
    assert max_calories(file_input_data) == 71506


def test_top_calories():
    assert top_calories(input_data) == 45000


def test_top_calories_from_file(file_input_data):
    assert top_calories(file_input_data) == 209603
