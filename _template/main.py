def function(data: list):
    return True


if __name__ == '__main__':
    with open('2021/day_XX/input.txt', 'r') as f:
        input_data = [int(i) for i in f.readlines()]
        print(f'Your result (1): {function(input_data)}')
        print(f'Your result (2): {function(input_data)}')
