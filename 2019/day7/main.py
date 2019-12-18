import itertools
import operator


class IntCodeComputer:
    """More advances intcode computer."""

    optcodes = {
        1: operator.add,
        2: operator.mul,
        3: 'input',
        4: 'output',
        5: True,   # jump-if-true
        6: False,  # jump-if-false
        7: operator.lt,
        8: operator.eq,
    }

    def __init__(self, intcode: str, inputs: list, debug: bool = False):
        """Initialize class instance."""
        self.intcode = intcode.strip().split(',')
        self.inputs = inputs
        self.evaluated = None
        self.printed_value = None
        self.debug = debug

    def run(self) -> str:
        """Mighty intcode computer."""
        self.pos, self.optcode = 0, 0

        while True:
            cursor = self.intcode[self.pos].zfill(5)
            if cursor.endswith('99'):
                break

            self.modes, optcode = cursor[:3], int(cursor[3:5])
            operation = self.optcodes.get(optcode)

            if optcode in (1, 2):  # Add/Multiply
                a = self.get_parameter(shift=1)
                b = self.get_parameter(shift=2)
                self.write_value(shift=3, value=operation(a, b))
                self.pos += 4
            elif optcode == 3:  # Input
                self.write_value(shift=1, value=self.inputs.pop())
                self.pos += 2
            elif optcode == 4:  # Output
                self.printed_value = self.get_parameter(shift=1)
                self.pos += 2
            elif optcode in (5, 6):  # Jump
                a = self.get_parameter(shift=1)
                b = self.get_parameter(shift=2)
                if (a != 0) is operation:
                    self.pos = b
                else:
                    self.pos += 3
            elif optcode in (7, 8):  # Less or equal
                a = self.get_parameter(shift=1)
                b = self.get_parameter(shift=2)
                self.write_value(shift=3, value=(1 if operation(a, b) else 0))
                self.pos += 4
            else:
                raise ValueError(f'Invalid optcode in {cursor}')

        self.evaluated = ','.join(self.intcode)
        return self.printed_value

    def get_parameter(self, shift: int):
        """Get parameter value."""
        mode = self.modes[-shift]
        value = self.intcode[self.pos + shift]

        if mode == '0':
            return int(self.intcode[int(value)])
        elif mode == '1':
            return int(value)
        else:
            raise ValueError(f'Invalud mode: {mode}')

    def write_value(self, shift: int, value: int):
        """Write value to intcode."""
        self.intcode[int(self.intcode[self.pos + shift])] = str(value)


class AmplificationCircuit:
    def __init__(self, intcode: str, amplifiers_range: range = range(0, 5)):
        """Initialize class instance."""
        self.intcode: str = intcode
        self.amplifiers_range: range = amplifiers_range

    def get_intcode_result(self, sequence: list) -> int:
        """Get ``IntCodeComputer`` result."""
        result = 0
        for i in sequence:
            result = IntCodeComputer(self.intcode, inputs=[result, i]).run()

        return result

    def get_highest_signal(self) -> int:
        """Get highest possible output signal."""
        return max(
            self.get_intcode_result(seq)
            for seq in itertools.permutations(self.amplifiers_range)
        )


if __name__ == '__main__':
    input_file = '2019/day7/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        intcode = f.readline()
        ac = AmplificationCircuit(intcode=intcode)
        print(f'Highest signal: {ac.get_highest_signal()}')  # 14902
