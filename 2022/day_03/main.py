from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def get_score(char: str) -> int:
    """Get score for a character."""
    initial = 'A' if char.isupper() else 'a'
    return ord(char) - ord(initial) + (27 if initial == 'A' else 1)


def get_common_items_in_each_rucksack(data: str) -> list[set]:
    """Find common items in each line between parts."""
    return [
        set(x[:len(x) // 2]) & set(x[len(x) // 2:])
        for x in data.splitlines()
    ]


def get_common_items_in_groups(data: str, group_size: int = 3) -> list[set]:
    """Find common items in groups of N."""
    data = data.splitlines()
    groups = [data[i:i + group_size] for i in range(0, len(data), group_size)]
    return [
        set.intersection(*(set(x) for x in g))
        for g in groups
    ]


def get_sum_score(common_items: list[set]) -> int:
    """Count sum score for common items."""
    return sum(get_score(char=list(c)[0]) for c in common_items)


def get_score_part_1(data: str) -> int:
    """Get total score for part 1."""
    common_items = get_common_items_in_each_rucksack(data)
    return get_sum_score(common_items)


def get_score_part_2(data: str) -> int:
    """Get total score for part 2."""
    common_items = get_common_items_in_groups(data)
    return get_sum_score(common_items)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_score_part_1(input_data)}')
        print(f'Your result (2): {get_score_part_2(input_data)}')
