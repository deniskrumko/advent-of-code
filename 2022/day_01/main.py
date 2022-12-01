def count_calories(data: list) -> list[int]:
    """Count calories per elf."""
    result = [0]
    for value in data:
        if value:
            result[-1] += int(value)
        else:
            result.append(0)
    return result


def max_calories(data: list) -> int:
    """Find max calories in data."""
    return max(count_calories(data))


def top_calories(data: list, top: int = 3) -> int:
    """Get sum of top 3 calories in data."""
    return sum(sorted(count_calories(data))[-top:])


if __name__ == '__main__':
    with open('2022/day_01/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {max_calories(input_data)}')
        print(f'Your result (2): {top_calories(input_data)}')
