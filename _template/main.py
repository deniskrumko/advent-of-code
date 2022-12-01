from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def function_1(data: str):
    return True


def function_2(data: str):
    return True


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
