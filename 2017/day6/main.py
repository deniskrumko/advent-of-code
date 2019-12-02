def memory_balancer(puzzle):
    steps = 0
    states = []
    length = len(puzzle)

    while tuple(puzzle) not in states:
        states.append(tuple(puzzle))
        max_number = max(puzzle)
        index = puzzle.index(max_number)
        amount = puzzle[index]
        puzzle[index] = 0

        while amount != 0:
            index += 1
            puzzle[index % length] += 1
            amount -= 1

        steps += 1

    first_occur = states.index(tuple(puzzle))
    cycle_steps = len(states) - first_occur

    return steps, cycle_steps


def main():
    with open('day6/input.txt', 'r') as f:
        puzzle = [int(x) for x in f.readline().split()]

    # puzzle = [0, 2, 7, 0]

    steps, last_cycle_steps = memory_balancer(puzzle)
    print(steps)
    print(last_cycle_steps)


if __name__ == '__main__':
    main()
