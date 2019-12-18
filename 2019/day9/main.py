import operator


class IntCode:
    """Class for storing int codes."""

    def __init__(self, initial_value: list):
        """Initialize class instance."""
        self.initial_value = initial_value
        self.memory = {}
        self.populate_memory()

    def populate_memory(self):
        """Populate memory with initial values."""
        index = 0
        for value in self.initial_value:
            self.memory[index] = value
            index += 1
        self.memory[index] = 0

    def __getitem__(self, index):
        """Get item from memory."""
        value = self.memory.get(index)
        if value is None:
            value = 0
            self.memory[index] = value
        return value

    def __setitem__(self, index, value):
        """Set item in memory."""
        self.memory[index] = value


class IntCodeComputer:
    """Perfect intcode computer (v4)."""

    optcodes = {
        1: operator.add,
        2: operator.mul,
        3: 'input',
        4: 'output',
        5: True,   # jump-if-true
        6: False,  # jump-if-false
        7: operator.lt,
        8: operator.eq,
        9: 'position',
    }

    def __init__(self, intcode: str, inputs: list, break_mode: bool = False):
        """Initialize class instance."""
        self.intcode = IntCode(intcode.strip().split(','))
        self.inputs = inputs
        self.printed_value = None
        self.all_printed_values = []
        self.pos = 0
        self.optcode = 0
        self.break_mode = break_mode
        self.halted = False
        self.relative_base = 0

    def __repr__(self):
        return f'<IntCodeComputer: inputs={self.inputs} pos={self.pos}>'

    def run(self) -> str:
        """Mighty intcode computer."""
        while True:
            cursor = self.intcode[self.pos].zfill(5)
            if cursor.endswith('99'):
                self.halted = True
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
                self.all_printed_values.append(self.printed_value)
                self.pos += 2
                if self.break_mode:
                    return self.printed_value
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
            elif optcode == 9:  # Change relative base
                value = self.get_parameter(shift=1)
                self.relative_base += value
                self.pos += 2
            else:
                raise ValueError(f'Invalid optcode in {cursor}')

        return self.printed_value

    def get_parameter(self, shift: int):
        """Get parameter value."""
        mode = self.modes[-shift]
        value = self.intcode[self.pos + shift]

        if mode == '0':    # Position mode
            return int(self.intcode[int(value)])
        elif mode == '1':  # Imeediate mode
            return int(value)
        elif mode == '2':  # Relative mode
            return int(self.intcode[int(value) + self.relative_base])
        else:
            raise ValueError(f'Invalud mode: {mode}')

    def write_value(self, shift: int, value: int):
        """Write value to intcode."""
        pos = int(self.intcode[self.pos + shift])
        mode = self.modes[-shift]

        if mode == '0':
            self.intcode[pos] = str(value)
        elif mode == '2':
            self.intcode[pos + self.relative_base] = str(value)
        else:
            raise ValueError(f'Invalud mode in `write_value`: {mode}')


if __name__ == '__main__':
    input_file = '2019/day9/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        intcode = f.readline()
        computer = IntCodeComputer(intcode, inputs=[1])
        computer.run()
        print(f'Boost code: {computer.all_printed_values}')  # 3241900951

        computer = IntCodeComputer(intcode, inputs=[2])
        computer.run()
        print(f'Coordinates: {computer.all_printed_values}')  # 83089
