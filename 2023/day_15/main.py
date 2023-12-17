from collections import (
    OrderedDict,
    defaultdict,
)
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def hasher(line: str) -> int:
    """Calculate hash value of line."""
    cur_val = 0
    for ch in line:
        cur_val += ord(ch)
        cur_val *= 17
        cur_val %= 256
    return cur_val


def handle_lenses_in_boxes(instructions: list[str]) -> dict[dict[str, int]]:
    """Add/remove lenses from boxes using instructions list."""
    boxes = defaultdict(OrderedDict)

    for instruction in instructions:
        parts = instruction.split('=')
        string, power = None, None

        if len(parts) == 2:  # instruction like ab=10
            string = parts[0]
            power = int(parts[1])
        elif instruction.endswith('-'):  # instruction like ab-
            string = instruction.strip('-')
        else:
            raise ValueError('wrong value')

        box = boxes[hasher(string)]
        if power is not None:
            box[string] = power
        else:
            box.pop(string, 0)

    return boxes


def get_focal_power(boxes: dict[dict[str, int]]) -> int:
    """Calculate focal power of lenses in boxes."""
    return sum(
        (box_index + 1) * (lens_index + 1) * value[1]
        for box_index, box in boxes.items()
        for lens_index, value in enumerate(box.items())
    )


def function_1(data: str) -> int:
    """Get result for puzzle (part 1)."""
    return sum(hasher(part) for part in data.strip().split(','))


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    boxes = handle_lenses_in_boxes(data.strip().split(','))
    return get_focal_power(boxes)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
