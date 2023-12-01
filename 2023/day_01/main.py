from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
DIGITS_LIST = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')


def get_border_int(line: str, replacement: list | None = None) -> int:
    """Get integer from first and last digit in string."""
    first = get_first_digit(line, replacement)
    last = get_first_digit(line, replacement, reversed=True)
    return int(first + last)


def get_first_digit(line: str, replacement: list | None = None, reversed: bool = False) -> str:
    """Get first occurence of digit in string."""
    buffer = ''
    for char in (line if not reversed else line[::-1]):
        if char.isdigit():
            return char

        if replacement:
            buffer = char + buffer if reversed else buffer + char
            for r_pos, r_val in enumerate(replacement, 1):
                if r_val in buffer:
                    return str(r_pos)

    raise ValueError(f'No digit found in string: {line}')


def function_1(data: str, replacement: list | None = None) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(get_border_int(line, replacement) for line in data.splitlines())


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data, DIGITS_LIST)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
