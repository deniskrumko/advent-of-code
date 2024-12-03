from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def is_safe_report_with_errors(report: list[int]) -> bool:
    """Check if report is safe with 1 allowed error."""
    for i in range(-1, len(report)):
        left = report[:i] if i >= 0 else []
        right = report[i + 1:]
        if is_safe_report(report=left + right):
            return True

    return False


def is_safe_report(report: list[int], min_allowed: int = 1, max_allowed: int = 3) -> bool:
    """Check if report is safe."""
    last_value = report[0]
    is_increasing = None

    for value in report[1:]:
        diff = abs(value - last_value)
        if not (min_allowed <= diff <= max_allowed):
            return False

        currently_increasing = value > last_value
        last_value = value

        if is_increasing is None:
            is_increasing = currently_increasing
            continue

        if is_increasing != currently_increasing:
            return False

    return True


def parse_report(line: str) -> list[int]:
    """Parse line with numbers."""
    return [int(v) for v in line.split()]


def function_1(data: str) -> int:
    """Get result for puzzle (part 1)."""
    return sum(is_safe_report(parse_report(line)) for line in data.splitlines())


def function_2(data: str) -> int:
    """Get result for puzzle (part 2)."""
    return sum(is_safe_report_with_errors(parse_report(line)) for line in data.splitlines())


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
