from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


@dataclass
class Block:
    """Block class."""

    values: list[str]
    length: int  # max size of block
    capacity: int  # how filled then block (0 -> empty)

    @classmethod
    def from_num(cls, i: int, num: int) -> 'Block':
        """Build block from iteration process."""
        if i % 2 == 1:
            return cls(  # empty block
                values=[],
                length=num,
                capacity=0,
            )

        return cls(
            values=[i // 2] * num,
            length=num,
            capacity=num,
        )

    @property
    def is_full(self) -> bool:
        """Check if block is full."""
        return self.capacity == self.length

    @property
    def is_empty(self) -> bool:
        """Check if block is empty."""
        return self.capacity == 0

    @property
    def empty_space(self) -> int:
        """Get empty space in block."""
        return self.length - self.capacity

    @property
    def has_empty(self) -> bool:
        """Check if block has empty space."""
        return self.capacity < self.length

    def add(self, value: int):
        """Add value to block."""
        # if self.is_full:
        #     raise ValueError('no space to add value')
        self.capacity += 1
        self.values.append(value)

    def pop(self) -> int:
        """Pop value from block."""
        # if self.is_empty:
        #     raise ValueError('no values to return')
        self.capacity -= 1
        return self.values.pop()

    def transfuse_to(self, recipient: 'Block'):
        """Transfuse values from self (donor) to recipient."""
        while True:
            recipient.add(self.pop())
            if recipient.is_full or self.is_empty:
                return

    def __str__(self):
        """Get string representation."""
        return ''.join(
            str(self.values[i]) if i < self.capacity else '.'
            for i in range(self.length)
        )


class Puzzle:
    """Puzzle class."""

    def __init__(self, data: str) -> 'Puzzle':
        """Initialize class instance."""
        self.blocks = tuple(
            Block.from_num(i, int(num))
            for i, num in enumerate(data.strip())
        )

    def __str__(self) -> str:
        """Get string representation."""
        return ''.join(str(b) for b in self.blocks)

    def compact(self) -> 'Puzzle':
        """Compact blocks."""
        left, right = 0, len(self.blocks) - 1

        while left < right:
            recipient = self.blocks[left]
            if recipient.is_full:
                left += 1
                continue

            donor = self.blocks[right]
            if donor.is_empty:
                right -= 1
                continue

            donor.transfuse_to(recipient)

        return self

    def compact_by_full_blocks(self) -> 'Puzzle':
        """Compact blocks by full blocks."""
        for right in range(len(self.blocks) - 1, 0, -1):
            donor = self.blocks[right]
            if donor.is_empty:
                continue

            for left in range(0, right):
                recipient = self.blocks[left]
                if not recipient.has_empty:
                    continue

                if recipient.empty_space >= donor.capacity:
                    donor.transfuse_to(recipient)
                    break

        return self

    @property
    def checksum(self) -> int:
        """Calculate result checksum."""
        total = 0
        i = 0

        for block in self.blocks:
            for value in block.values:
                total += value * i
                i += 1

            i += block.empty_space

        return total


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    p = Puzzle(data).compact()
    return p.checksum


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    p = Puzzle(data).compact_by_full_blocks()
    return p.checksum


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
