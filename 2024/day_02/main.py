from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'

def check_with_problem_damp(report):
    values = [int(v) for v in report.split()]
    for skip in range(len(values)):
        v = values[:]
        v.pop(skip)
        if is_safe_report(report=' '.join(str(i) for i in v)):
            return True

    return False

def is_safe_report(
    report: str,
    *,
    min_allowed: int = 1,
    max_allowed: int = 3,
    problem_damp: bool = False,
) -> bool:
    """Check if report is safe."""
    last_value = None
    is_increasing = None

    for pos, value in enumerate(int(v) for v in report.split()):
        if last_value is None:
            last_value = value
            continue

        diff = abs(value - last_value)
        if diff < min_allowed or diff > max_allowed:
            return check_with_problem_damp(report) if problem_damp else False

        currently_increasing = value > last_value

        if is_increasing is None:
            is_increasing = currently_increasing
            last_value = value
            continue

        if is_increasing != currently_increasing:
            return check_with_problem_damp(report) if problem_damp else False

        last_value = value

    return True


def function_1(data: str, problem_damp: bool = False) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(is_safe_report(line, problem_damp=problem_damp) for line in data.splitlines())


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data, problem_damp=True)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
