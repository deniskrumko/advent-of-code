import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 8


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 2285


def test_function_2():
    assert function_2(input_data) == 2286


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 77021
