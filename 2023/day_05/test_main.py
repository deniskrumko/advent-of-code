import pytest

from .main import (
    INPUT_FILE,
    function_1,
    function_2,
)

input_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 35


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 26273516


def test_function_2():
    assert function_2(input_data) == 46


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 34039469
