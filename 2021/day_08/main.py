from collections import (
    Counter,
    OrderedDict,
)

DIGITS_MAP = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

INVERTED_DIGITS_MAP = {v: k for k, v in DIGITS_MAP.items()}


def parse_line(line: str) -> tuple[list]:
    """Parse single line to two lists of input and output values."""
    two_parts = line.split('|')
    return tuple(part.split() for part in two_parts)


def get_unique_lengths() -> set:
    """Get set of unique lengths from digits map."""
    lengths = Counter([len(value) for value in DIGITS_MAP.values()])
    return {length for length, count in lengths.items() if count == 1}


def count_unique_values(data: list) -> int:
    """Count amount of unique-length values from input data."""
    unique_lengths: set = get_unique_lengths()
    return len([
        output_value
        for line in data
        for output_value in parse_line(line)[1]
        if len(output_value) in unique_lengths
    ])


def check_possible_mapping(possible_mapping: dict, input_values: list) -> bool:
    """Check if possible mapping is correct or not."""
    decoded_values = []
    for value in input_values:
        decoded_value = ''.join(sorted(possible_mapping[c] for c in value))
        decoded_values.append(decoded_value)

    return sorted(decoded_values) == sorted(DIGITS_MAP.values())


def find_correct_mapping(result_map: dict, input_values: list) -> dict:
    """Iterate through all possible mappings to find correct one."""
    keys = list(result_map)

    # This is so bad, but it works :(
    for c_1 in result_map[keys[0]]:
        for c_2 in result_map[keys[1]]:
            for c_3 in result_map[keys[2]]:
                for c_4 in result_map[keys[3]]:
                    for c_5 in result_map[keys[4]]:
                        for c_6 in result_map[keys[5]]:
                            for c_7 in result_map[keys[6]]:
                                values = [c_1, c_2, c_3, c_4, c_5, c_6, c_7]
                                if len(set(values)) != 7:
                                    continue

                                possible_mapping = {keys[i]: values[i] for i in range(7)}
                                if check_possible_mapping(possible_mapping, input_values):
                                    return possible_mapping

    raise ValueError('No possible choice')


def decode_output_value(line: str) -> int:
    """Parse single line, find correct mapping and decode output value."""
    input_values, output_values = parse_line(line)
    unique_lengths: set = get_unique_lengths()
    length_to_digit_map: dict = {
        len(v): d for d, v in DIGITS_MAP.items() if len(v) in unique_lengths
    }

    # Populate first guess map
    guess_map: dict = OrderedDict()
    for value in input_values:
        if len(value) in unique_lengths:
            guessed_digit = length_to_digit_map[len(value)]
            guess_map[guessed_digit] = value

    # Add possible guesses to result map
    result_map: dict = {}
    for digit in sorted(guess_map, key=lambda x: len(guess_map[x])):
        values = guess_map[digit]
        original_values = DIGITS_MAP[digit]
        for char in values:
            if char in result_map:
                continue

            result_map.setdefault(char, set())
            for original_value in original_values:
                result_map[char].add(original_value)

    # Just to be sure that all values populated
    assert len(result_map) == 7

    # Find correct mapping among all mappings
    correct_mapping: dict = find_correct_mapping(result_map, input_values)

    # Decode each digit of output value
    result_digits_str = ''
    for output_value in output_values:
        decoded_value = ''.join(sorted(correct_mapping[c] for c in output_value))
        result_digits_str += str(INVERTED_DIGITS_MAP[decoded_value])

    # Return integer result
    return int(result_digits_str)


def get_total_four_digit_values(data: list):
    return sum(decode_output_value(line) for line in data)


if __name__ == '__main__':
    with open('2021/day_08/input.txt', 'r') as f:
        input_data = [i.strip() for i in f.readlines()]
        print(f'Your result (1): {count_unique_values(input_data)}')
        print(f'Your result (2): {get_total_four_digit_values(input_data)}')
