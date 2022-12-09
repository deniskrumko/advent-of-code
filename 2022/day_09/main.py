from pathlib import Path

import numpy as np

INPUT_FILE = Path(__file__).parent / 'input.txt'
DIRECTIONS = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}


def move_knot(head_pos: np.ndarray, tail_pos: np.ndarray) -> np.ndarray:
    """Move tail towards head depending on position."""
    # check if head and tail are equal (vector operation)
    equal = head_pos == tail_pos

    # if head and tail on same spot - don't move
    if equal.all():
        return tail_pos

    # if head and tail on same line (horizontal or vertical) - move (or not)
    if equal.any():
        # get coordinate - x (0) or y (1) where head and tail are not equal (ne)
        ne_pos = np.where(equal == 0)[0][0]

        # if two knots touching - don't move tail
        if abs(head_pos[ne_pos] - tail_pos[ne_pos]) == 1:
            return tail_pos

        # check that head and tail a two moves apart
        assert abs(head_pos[ne_pos] - tail_pos[ne_pos]) == 2

        # move tail by 1 position towards head
        tail_pos[ne_pos] += 1 if head_pos[ne_pos] > tail_pos[ne_pos] else -1
        return tail_pos

    # if head and tail are diagonally touched - don't move tail
    if np.all(np.absolute(tail_pos - head_pos) == 1):
        return tail_pos

    # if head and tail more than 2 spots apart -> move tail diagonally
    moves = (head_pos > tail_pos).astype(int)
    moves[moves == 0] = -1
    tail_pos += moves
    return tail_pos


def simulate_rope_bridge(data: str, knots: int) -> int:
    """Get result for puzzle."""
    ropes = np.zeros((knots, 2))
    tail_moves = set()

    for command in data.splitlines():
        direction, moves = command.split(' ')
        step = DIRECTIONS[direction]

        for _ in range(int(moves)):
            for k in range(knots):
                if k == 0:
                    # move head knot
                    ropes[0] = np.add(ropes[0], step)
                else:
                    # move other knots
                    ropes[k] = move_knot(ropes[k - 1], ropes[k])

            # log tail knot position
            tail_moves.add(tuple(ropes[-1]))

    return len(tail_moves)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {simulate_rope_bridge(input_data, knots=2)}')
        print(f'Your result (2): {simulate_rope_bridge(input_data, knots=10)}')
