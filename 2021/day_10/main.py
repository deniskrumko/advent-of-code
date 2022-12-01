PAIRS = ['[]', '()', '<>', '{}']
LEFT_ONLY = [p[0] for p in PAIRS]
RIGHT_ONLY = [p[1] for p in PAIRS]
CORRUPTED_SCORE_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_SCORE_MAP = {')': 1, ']': 2, '}': 3, '>': 4}


def parse_line(line: str) -> tuple:
    """Check if line correct, incomplete or corrupted.

    First value of result is "success":
        True -> line is correct
        None -> line is incomplete
        False -> line is corrupted

    Second value of result is "remaining line" after parsing.
    """
    success = True
    while line:
        found = False
        for pair in PAIRS:
            if pair in line:
                line = line.replace(pair, '')
                found = True

        if not found:
            is_incomplete = all(value in LEFT_ONLY for value in line)
            success = None if is_incomplete else False
            break

    return success, line


def count_syntax_checker_points_for_corrupted(data: list) -> int:
    """Count total score for syntax checker (corrupted lines only)."""
    checked_lines = [parse_line(line) for line in data]
    corrupted_lines = [pair[1] for pair in checked_lines if pair[0] is False]

    total_score = 0
    for corrupted_line in corrupted_lines:
        for value in corrupted_line:
            if value in CORRUPTED_SCORE_MAP:
                total_score += CORRUPTED_SCORE_MAP[value]
                break

    return total_score


def get_score_for_incomplete_line(line: str) -> tuple:
    """Get score for incomplete line.

    First value of result is line score, second value is "completion line".
    """
    success, remaining_line = parse_line(line)
    assert success is None

    reversed_line = ''.join(RIGHT_ONLY[LEFT_ONLY.index(c)] for c in reversed(remaining_line))
    assert parse_line(remaining_line + reversed_line)[0] is True  # check that total line is correct

    line_score = 0
    for value in reversed_line:
        line_score *= 5
        line_score += INCOMPLETE_SCORE_MAP[value]

    return line_score, reversed_line


def count_syntax_checker_points_for_incomplete(data: list) -> int:
    """Count total score for syntax checker (incomplete lines only)."""
    checked_lines = [parse_line(line) for line in data]
    incompleted_lines = [pair[1] for pair in checked_lines if pair[0] is None]
    line_scores = [get_score_for_incomplete_line(line)[0] for line in incompleted_lines]
    return sorted(line_scores)[len(line_scores) // 2]


if __name__ == '__main__':
    with open('2021/day_10/input.txt', 'r') as f:
        input_data = [i.strip() for i in f.readlines()]
        print(f'Your result (1): {count_syntax_checker_points_for_corrupted(input_data)}')
        print(f'Your result (2): {count_syntax_checker_points_for_incomplete(input_data)}')
