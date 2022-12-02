from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'

ABC_CODES = 'ABC'
XYZ_CODES = 'XYZ'
GAMES_LEN = len(ABC_CODES)


def prepare_data(data: str) -> list[list[str]]:
    """Parse data."""
    return [val.split() for val in data.splitlines()]


def get_game_score(op_move: str, my_move: str) -> int:
    """Get result game score."""
    op_index = ABC_CODES.index(op_move)
    my_index = XYZ_CODES.index(my_move)

    if (my_index - 1) % GAMES_LEN == op_index:
        score = 6
    elif my_index == op_index:
        score = 3
    else:
        score = 0

    score += (my_index + 1)
    return score


def get_total_score(data: str) -> int:
    """Get total score with initial rules (part 1)."""
    return sum(get_game_score(*x) for x in prepare_data(data))


def choose_my_move(op_move: str, game_result: str) -> str:
    """Choose own move depending on opponent move and expected result."""
    op_index = ABC_CODES.index(op_move)
    shift = XYZ_CODES.index(game_result) - 1  # X (-1) - loose, Y (0) - draw, Z (1) - win
    return XYZ_CODES[(op_index + shift) % GAMES_LEN]


def get_total_score_with_new_rules(data: str):
    """Get total score with modified rules (part 2)."""
    games = [
        [op_move, choose_my_move(op_move, game_result)]
        for op_move, game_result in prepare_data(data)
    ]
    return sum(get_game_score(*x) for x in games)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_total_score(input_data)}')
        print(f'Your result (2): {get_total_score_with_new_rules(input_data)}')
