import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 62


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 35244


def test_function_2():
    assert function_2(input_data) == 952408144115


@pytest.mark.skip('Not ready')
def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data)
