from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Dict,
    Union,
)


@dataclass
class Bag:
    """Class for bag."""

    color: str
    parents: dict = field(default_factory=dict)
    childs: dict = field(default_factory=dict)

    def add_relation(self, bag, amount: int, is_parent: bool):
        """Add bag relation."""
        relation_field = self.parents if is_parent else self.childs
        relation_field[bag] = amount

    def get_ancestors(self) -> set:
        """Get set of all bag ancestors."""
        result = set()
        for parent in self.parents:
            result |= {parent} | parent.get_ancestors()
        return result

    def get_capacity(self) -> int:
        """Get bag capacity (amount of bags inside it)."""
        amount = 0
        for child_bag, child_amount in self.childs.items():
            amount += (child_amount * (child_bag.get_capacity() + 1))
        return amount

    def __hash__(self) -> int:
        """Get hash from ``Bag`` object."""
        return hash(self.color)

    def __repr__(self):
        """Representation of ``Bag`` object."""
        return f'<Bag: {self.color}>'


def build_bags_graph(input_data: str) -> Dict[str, Bag]:
    """Build bags relations graph and populate result dict."""
    bags = {}

    def get_bag_by_color(color: Union[str, list]) -> Bag:
        color = color.strip() if isinstance(color, str) else ' '.join(color)
        if color not in bags:
            bags[color] = Bag(color=color)
        return bags[color]

    for line in input_data.strip().split('\n'):
        parent_str, childs_str = line[:-1].split('contain')
        parent_color, _ = parent_str.strip().rsplit(' ', 1)
        parent_bag = get_bag_by_color(color=parent_color)

        for child in childs_str.split(','):
            amount, *child_color, _ = child.strip().split()
            if amount != 'no':  # For case: <color> bags contain no other bags
                child_bag = get_bag_by_color(color=child_color)
                amount = int(amount)
                parent_bag.add_relation(child_bag, amount, is_parent=False)
                child_bag.add_relation(parent_bag, amount, is_parent=True)

    return bags


def get_bag_parents_amount(input_data: str, color: str = 'shiny gold') -> int:
    """Get total amount of bags that can contain requested bag."""
    bags = build_bags_graph(input_data)
    return len(bags[color].get_ancestors())


def get_bag_childs_amount(input_data: str, color: str = 'shiny gold') -> int:
    """Get total amount of bags that requested bag must contain."""
    bags = build_bags_graph(input_data)
    return bags[color].get_capacity()


if __name__ == '__main__':
    with open('2020/day_07/input.txt', 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_bag_parents_amount(input_data)}')
        print(f'Your result (2): {get_bag_childs_amount(input_data)}')
