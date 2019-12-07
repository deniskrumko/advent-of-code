import pytest

from .main import IntCodeComputer

large_example = (
    '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,'
    '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
    '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
)


@pytest.mark.parametrize('input_code,evaluated,input_value', [
    ('1002,4,3,4,33', '1002,4,3,4,99', 0),
    ('3,0,4,0,99', '5,0,4,0,99', 5),
])
def test_intcode_computer(input_code, evaluated, input_value):
    computer = IntCodeComputer(input_code, input_value)
    computer.run()
    assert computer.evaluated == evaluated


@pytest.mark.parametrize('input_code,last_output,input_value', [
    (large_example, 999, 1),
    (large_example, 1000, 8),
    (large_example, 1001, 20),
])
def test_output_of_intcode_computer(input_code, last_output, input_value):
    assert IntCodeComputer(input_code, input_value).run() == last_output
