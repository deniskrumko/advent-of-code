import math
import re
from collections import defaultdict
from itertools import cycle
from pathlib import Path
from typing import Callable

INPUT_FILE = Path(__file__).parent / 'input.txt'
START_NODE, END_NODE = 'AAA', 'ZZZ'
START_CHAR, END_CHAR = 'A', 'Z'


class Node:
    """Class for storing node and left/right neighboor."""

    name: str = None
    left: 'Node' = None
    right: 'Node' = None

    def __repr__(self):
        return f'<Node: {self.name}>'

    def make_step(self, command: str) -> 'Node':
        return self.left if command == 'L' else self.right

    def walk(self, instructions: str, is_finished: Callable) -> int:
        """Walk instructions until reaching the end."""
        cur, steps = self, 0
        for command in cycle(instructions):
            if is_finished(cur):
                return steps
            cur = cur.make_step(command)
            steps += 1


def parse_data(data: str) -> tuple[str, dict[str, Node]]:
    """Parse initial data to instructions and nodes."""
    nodes = defaultdict(Node)
    instructions = None

    for line in data.splitlines():
        if instructions is None:
            instructions = line
            continue

        if not line:
            continue

        m = re.match(r'(?P<node>\w{3}) = \((?P<left>\w{3}), (?P<right>\w{3})\)', line).groupdict()
        node = nodes[m['node']]
        node.name = m['node']
        node.left = nodes[m['left']]
        node.right = nodes[m['right']]

    return instructions, nodes


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    instructions, nodes = parse_data(data)
    return nodes[START_NODE].walk(instructions, is_finished=lambda n: n.name == END_NODE)


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    instructions, nodes = parse_data(data)
    steps_taken = (
        node.walk(instructions, is_finished=lambda n: n.name.endswith(END_CHAR))
        for node in nodes.values()
        if node.name.endswith(START_CHAR)
    )
    return math.lcm(*steps_taken)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
