from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def get_first_unique_packet(data: str, window: int = 4) -> int:
    """Find index of unique packet for window size."""
    for i in range(len(data)):
        if len(set(data[i:i + window])) == window:
            return i + window


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read().strip()
        print(f'Your result (1): {get_first_unique_packet(input_data, 4)}')
        print(f'Your result (2): {get_first_unique_packet(input_data, 14)}')
