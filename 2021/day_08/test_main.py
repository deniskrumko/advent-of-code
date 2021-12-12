import pytest

from .main import (
    count_unique_values,
    decode_output_value,
    get_total_four_digit_values,
)

input_data = '''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''.strip().split('\n')

input_data_2 = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'  # noqa


@pytest.fixture
def file_input_data():
    with open('2021/day_08/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def test_count_unique_values():
    assert count_unique_values(input_data) == 26


def test_count_unique_values_from_file(file_input_data):
    assert count_unique_values(file_input_data) == 512


def test_decode_output_value():
    assert decode_output_value(input_data_2) == 5353


def test_decode_output_value_for_all_input_data():
    expected_outputs = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    for i, expected_output in enumerate(expected_outputs):
        assert decode_output_value(input_data[i]) == expected_output


def test_get_total_four_digit_values():
    assert get_total_four_digit_values(input_data) == 61229


def test_function_2_from_file(file_input_data):
    assert get_total_four_digit_values(file_input_data) == 1091165
