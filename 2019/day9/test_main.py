import pytest


from .main import IntCodeComputer


def test_new_intcode_computer():
    intcode = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    computer = IntCodeComputer(intcode, inputs=[])
    computer.run()
    assert intcode == ','.join(str(v) for v in computer.all_printed_values)


def test_new_intcode_computer_2():
    intcode = '1102,34915192,34915192,7,4,7,99,0'
    computer = IntCodeComputer(intcode, inputs=[])
    assert len(str(computer.run())) == 16


def test_new_intcode_computer_3():
    intcode = '104,1125899906842624,99'
    computer = IntCodeComputer(intcode, inputs=[])
    assert computer.run() == 1125899906842624


@pytest.mark.parametrize('intcode,expected', (
    ('109, -1, 4, 1, 99', -1),
    ('109, -1, 104, 1, 99', 1),
    ('109, 1, 9, 2, 204, -6, 99', 204),
    ('109, 1, 109, 9, 204, -6, 99', 204),
    ('109, 1, 209, -1, 204, -106, 99', 204),
    ('109, 1, 3, 3, 204, 2, 99', 12345),
    ('109, 1, 203, 2, 204, 2, 99', 12345),
))
def test_new_intcode_computer_extra_tests(intcode, expected):
    computer = IntCodeComputer(intcode, inputs=[12345])
    result = computer.run()
    assert result == expected
