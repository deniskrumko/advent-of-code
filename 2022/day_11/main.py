import math
import re
from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def parse_m(monkey):
    lines = monkey.splitlines()
    return {
        'items': [int(i) for i in re.findall(r'\d+', lines[1])],
        'operation': re.search('.+new = (?P<op>.+)', lines[2]).groupdict()['op'],
        'test': int(re.search(r'\d+', lines[3]).group()),
        'if_true': int(re.search(r'\d+', lines[4]).group()),
        'if_false': int(re.search(r'\d+', lines[5]).group()),
    }


def function_1(data: str, rounds: int = 20, divide: bool = True) -> bool:
    """Get result for puzzle (part 1)."""
    monkeys = [parse_m(m) for m in data.split('\n\n')]
    stats = defaultdict(int)
    for i in range(rounds):
        for im, m in enumerate(monkeys):
            for i in m['items']:
                stats[im] += 1
                new_level = eval(m['operation'].replace('old', 'i'))
                if divide:
                    bored_level = math.floor(new_level / 3)
                else:
                    bored_level = new_level

                to_monkey = None
                if bored_level % m['test'] == 0:
                    to_monkey = m['if_true']
                else:
                    to_monkey = m['if_false']
                monkeys[to_monkey]['items'].append(bored_level)
            m['items'] = []

    return math.prod(sorted(stats.values())[-2:])


def function_2(data: str, rounds: int = 10000) -> bool:
    """Get result for puzzle (part 1)."""
    monkeys = [parse_m(m) for m in data.split('\n\n')]
    stats = defaultdict(int)
    for r in range(rounds):
        if r == 5000:
            print(stats.values())
            raise ValueError('I AM STUCK ON THIS, GOODBYE!')

        for im, m in enumerate(monkeys):
            oper = m['operation']
            test = m['test']

            for item in m['items']:
                bored_level = item
                stats[im] += 1

                if '+' in oper:
                    bored_level += int(oper.split(' + ')[-1])

                to_monkey = None
                if bored_level % test == 0:
                    to_monkey = m['if_true']
                else:
                    to_monkey = m['if_false']
                monkeys[to_monkey]['items'].append(bored_level)
            m['items'] = []

    return math.prod(sorted(stats.values())[-2:])


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
