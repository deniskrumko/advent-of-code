import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
    hasher,
)

input_data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_hasher():
    assert hasher('HASH') == 52


def test_function_1():
    assert function_1(input_data) == 1320


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 513172


def test_function_2():
    assert function_2(input_data) == 145


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 237806
