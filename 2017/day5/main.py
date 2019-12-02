def jump_maze(puzzle):
    steps = 0
    index = 0
    lenght = len(puzzle)

    while True:
        jump = puzzle[index]
        puzzle[index] = jump + 1
        index += jump
        steps += 1

        if index < 0 or index >= lenght:
            return steps


def jump_maze_2(puzzle):
    steps = 0
    index = 0
    lenght = len(puzzle)

    while True:
        jump = puzzle[index]

        if jump >= 3:
            shift = -1
        else:
            shift = 1

        puzzle[index] = jump + shift
        index += jump
        steps += 1

        if index < 0 or index >= lenght:
            return steps


def main():
    with open('day5/input.txt', 'r') as f:
        puzzle = [int(line) for line in f.readlines()]

    # puzzle = [0, 3, 0, 1, -3]

    steps = jump_maze_2(puzzle)
    print(steps)


if __name__ == '__main__':
    main()
