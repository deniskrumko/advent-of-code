import pytest

from .main import (
    intcode_to_list,
    intcode_to_str,
    run_intcode,
    intcode_computer,
    find_values,
)


@pytest.mark.parametrize('input_code,output_code', [
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
])
def test_intcode_computer(input_code, output_code):
    input_code = intcode_to_list(input_code)
    processed_code = intcode_computer(input_code)
    assert intcode_to_str(processed_code) == output_code


@pytest.mark.parametrize('a,b,expected', [
    (12, 2, 3267740),
])
def test_run_intcode(a, b, expected):
    input_file = '2019/day2/input.txt'
    assert run_intcode(input_file, a=a, b=b) == expected


@pytest.mark.parametrize('expected,a,b', [
    (19690720, 78, 70),
])
def test_find_values(a, b, expected):
    input_file = '2019/day2/input.txt'
    assert find_values(input_file, expected) == (a, b)
