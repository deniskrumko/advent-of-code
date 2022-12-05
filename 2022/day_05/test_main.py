import pytest

from .main import (
    INPUT_FILE,
    get_cratemover_9000_result,
    get_cratemover_9001_result,
)

input_data = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_get_cratemover_9000_result():
    assert get_cratemover_9000_result(input_data) == 'CMZ'


def test_get_cratemover_9000_result_from_file(file_input_data):
    assert get_cratemover_9000_result(file_input_data) == 'TQRFCBSJJ'


def test_get_cratemover_9001_result():
    assert get_cratemover_9001_result(input_data) == 'MCD'


def test_get_cratemover_9001_result_from_file(file_input_data):
    assert get_cratemover_9001_result(file_input_data) == 'RMHFJNVFP'
