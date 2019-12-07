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

    def __init__(self, intcode: str, input_value: int = 1):
        """Initialize class instance."""
        self.intcode = intcode.strip().split(',')
        self.input_value = input_value
        self.evaluated = None
        self.printed_value = None

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
                self.write_value(shift=1, value=self.input_value)
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


if __name__ == '__main__':
    input_file = '2019/day5/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        intcode = f.readline()

        computer = IntCodeComputer(intcode=intcode, input_value=1)
        print(f'Last printed value: {computer.run()}')  # 9431221

        computer = IntCodeComputer(intcode=intcode, input_value=5)
        print(f'Diagnostic: {computer.run()}')  # 1409363
