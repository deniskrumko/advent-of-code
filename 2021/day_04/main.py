from copy import deepcopy


def build_boards(data: list) -> list[list]:
    """Build boards from input data."""
    boards, new_board = [], []
    for line in (data[2:] + ['']):
        if line == '':
            boards.append(new_board)
            new_board = []
            continue

        line_int = [int(i) for i in line.split()]
        new_board.append(line_int)

    return boards


def check_board_has_won(board: list) -> bool:
    """Check if board won or not."""
    for row in board:
        if row.count('X') == 5:
            return True

    for i in range(5):
        if [board[j][i] for j in range(5)].count('X') == 5:
            return True

    return False


def get_winning_numbers(data: list) -> list[int]:
    """Get list of winning numbers."""
    return [int(i) for i in data[0].split(',')]


def get_board_score(board: list, win_number: int) -> int:
    """Get winning board score."""
    total = sum(sum([i for i in row if i != 'X']) for row in board)
    return total * win_number


def mark_boards(board: list, win_number: int):
    """Mark board with winning number."""
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == win_number:
                board[i][j] = 'X'


def bingo_first_winner(data: list) -> int:
    """Find bingo for first winner."""
    boards = build_boards(data)
    for win_number in get_winning_numbers(data):
        for board in boards:
            mark_boards(board, win_number)

        for board in boards:
            if check_board_has_won(board):
                return get_board_score(board, win_number)


def bingo_last_winner(data: list) -> int:
    """Find bingo for last winner."""
    boards = build_boards(data)
    for win_number in get_winning_numbers(data):
        for board in boards:
            mark_boards(board, win_number)

        for board in deepcopy(boards):
            if check_board_has_won(board):
                if len(boards) == 1:
                    return get_board_score(board, win_number)

                boards.remove(board)


if __name__ == '__main__':
    with open('2021/day_04/input.txt', 'r') as f:
        input_data = [i.strip() for i in f.readlines()]
        print(f'Your result (1): {bingo_first_winner(input_data)}')
        print(f'Your result (2): {bingo_last_winner(input_data)}')
