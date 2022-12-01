from collections import (
    Counter,
    defaultdict,
)


def lanternfish_cycle(data: list, days: int) -> int:
    """Imitate lanternfish life cycle."""
    fishes = Counter(data)

    for _ in range(days):
        new_fishes = defaultdict(int)
        for fish_age, fish_number in fishes.items():
            if fish_age == 0:
                new_fishes[8] += fish_number
                new_fishes[6] += fish_number
                continue

            new_fishes[fish_age - 1] += fish_number
        fishes = new_fishes

    return sum(fishes.values())


if __name__ == '__main__':
    with open('2021/day_06/input.txt', 'r') as f:
        input_data = [int(i) for i in f.read().split(',')]
        print(f'Your result (1): {lanternfish_cycle(input_data, days=80)}')
        print(f'Your result (2): {lanternfish_cycle(input_data, days=256)}')
