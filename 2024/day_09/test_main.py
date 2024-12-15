import pytest

from .main import (
    INPUT_FILE,
    Puzzle,
    function_1,
    function_2,
)

input_data = "2333133121414131402"


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

@pytest.mark.parametrize('value, expected', (
    ('12345', '0..111....22222'),
    ('222222212121212121215', '00..11..22..33.44.55.66.77.88.99.1010101010'),
    ('233313312141413140256', '00...111...2...333.44.5555.6666.777.888899.....101010101010'),
    ('2333133121414131402', '00...111...2...333.44.5555.6666.777.888899'),
))
def test_string_repr(value, expected):
    p = Puzzle(value)
    assert str(p) == expected


@pytest.mark.parametrize('value, expected', (
    ('12345', '022111222......'),
    ('2333133121414131402', '0099811188827773336446555566..............'),
    ('233313312141413140211', '001099111888287733374465555666...............'),
))
def test_compacted(value, expected):
    p = Puzzle(value).compact()
    assert str(p) == expected


@pytest.mark.parametrize('value, expected', (
    ('2333133121414131402', '00992111777.44.333....5555.6666.....8888..'),
))
def test_compact_by_full_blocks(value, expected):
    p = Puzzle(value).compact_by_full_blocks()
    assert str(p) == expected


@pytest.mark.parametrize('value, expected', (
    (input_data, 1928),
    ('111111111111111111111', 290),
    ('233313312141413140256', 3383),
))
def test_function_1(value, expected):
    assert function_1(value) == expected


def test_function_1_from_file(file_input_data):
    # 16401893 too low
    # 23896 too low of course
    assert function_1(file_input_data) == 6337367222422


@pytest.mark.parametrize('value, expected', (
    (input_data, 2858),
    ('1313165', 169),
))
def test_function_2(value, expected):
    assert function_2(value) == expected


def test_function_2_from_file(file_input_data):
    # 85099567236 too low
    # 6361539797932 too high
    assert function_2(file_input_data) == 6361380647183
