from collections import (
    Counter,
    defaultdict,
)


def build_template_from_str(template_str: str) -> dict:
    template = defaultdict(int)
    for i in range(len(template_str) - 1):
        pair = template_str[i:i + 2]
        assert len(pair) == 2
        template[pair] += 1
    return template


def parse_data(data: list) -> tuple[dict, dict]:
    template = build_template_from_str(template_str=data[0])

    rules = {}
    for line in data[2:]:
        key, value = line.split(' -> ')
        rules[key] = value

    return template, rules


def polymerization_step(template: str, rules: dict) -> None:
    produced_elements = defaultdict(int)
    for pair, count in template.items():
        for new_pair in (pair[0] + rules[pair], rules[pair] + pair[1]):
            produced_elements[new_pair] += count

    template.clear()
    template.update(produced_elements)


def apply_polymerization_by_steps(template: dict, rules: dict, steps: int) -> None:
    for _ in range(steps):
        polymerization_step(template, rules)


def get_elements_count(template: dict) -> dict:
    elements = defaultdict(int)
    last_element = None

    for pair, count in template.items():
        first_element, second_element = pair
        if first_element != last_element:
            elements[first_element] += count

        elements[second_element] += count
        last_element = second_element
    return elements


def find_most_and_least_common_score(data: list, steps: int = 10) -> int:
    # Apply N steps on initial template by rules
    template, rules = parse_data(data)
    apply_polymerization_by_steps(template, rules, steps)

    # Find most and least common elements and get result score
    elements = get_elements_count(template)

    elements = Counter(template)
    least_common, *_, most_common = sorted(elements, key=lambda x: elements[x])
    return elements[most_common] - elements[least_common]


if __name__ == '__main__':
    with open('2021/day_14/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {find_most_and_least_common_score(input_data)}')
        # print(f'Your result (2): {find_most_and_least_common_score(input_data, 40)}')
