import re
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
START = 'in'


class Part:
    def __init__(self, part_str: str):
        """Initialize class instance."""
        self.values = {}
        for part in part_str[1:-1].split(','):
            name, value = part.split('=')
            self.values[name] = int(value)

    @property
    def rating(self) -> int:
        return sum(self.values.values())


class Cond:
    def __init__(self, cond_str):
        """Initialize class instance."""
        if ':' in cond_str:
            match = re.match(r'^(?P<param>\w+)(?P<oper>.)(?P<num>\d+):(?P<dest>.+)$', cond_str)
            self.param = match['param']
            self.oper = match['oper']
            self.num = int(match['num'])
            self.dest = match['dest']
            self.immediate = None
        else:
            self.immediate = cond_str

    def is_applied(self, part: Part):
        if self.immediate:
            return True

        part_value = part.values[self.param]
        if self.oper == '>':
            return part_value > self.num
        elif self.oper == '<':
            return part_value < self.num
        else:
            raise ValueError('...')

    @property
    def next_rule_name(self) -> str:
        return self.immediate or self.dest


class Rule:
    def __init__(self, rule_str: str):
        """Initialize class instance."""
        match = re.match(r'^(?P<name>.+){(?P<other>.+)}$', rule_str).groupdict()
        self.name = match['name']
        self.conditions = [Cond(part) for part in match['other'].split(',')]

    def get_next_rule_name(self, part: Part) -> str:
        for cond in self.conditions:
            if cond.is_applied(part):
                return cond.next_rule_name

        raise ValueError('Not found')


def parse(data: str):
    rules, parts = {}, []
    rules_raw, parts_raw = data.split('\n\n')
    for rule_str in rules_raw.splitlines():
        rule = Rule(rule_str)
        rules[rule.name] = rule

    for part_str in parts_raw.splitlines():
        part = Part(part_str)
        parts.append(part)

    return rules, parts


def part_is_accepted(part, rules):
    cur = START
    while True:
        rule = rules[cur]
        cur = rule.get_next_rule_name(part)
        if cur == 'A':
            return True
        if cur == 'R':
            return False


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    rules, parts = parse(data)

    return sum(
        part.rating
        for part in parts
        if part_is_accepted(part, rules)
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return True


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
