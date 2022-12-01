from collections import Counter
from functools import partial


class SpaceImageFormatDecoder:
    """Class for decoding and rendering space image format."""

    def __init__(self, data: str, width: int, height: int):
        """Initialize class instance."""
        self.data = data
        self.width = width
        self.height = height
        self.layers = self.get_layers()

    def get_layers(self):
        """Get layers from initial data."""
        result = []
        layer_chunk = self.width * self.height

        for j in range(len(self.data) // layer_chunk):
            chunk = self.data[layer_chunk * j: layer_chunk * (j + 1)]
            layer = [
                chunk[self.width * i: self.width * (i + 1)]
                for i in range(self.height)
            ]
            result.append(layer)

        return result

    def get_checksum(self) -> int:
        """Find layer with least 0 and count checksum."""
        layer = min(self.layers, key=partial(self.count_digits, 0))
        return self.count_digits(1, layer) * self.count_digits(2, layer)

    def count_digits(self, digit: int, layer: list) -> int:
        """Count specified digits on layer."""
        layer_as_str = ''.join(layer)
        counter = Counter(layer_as_str)
        return counter.get(str(digit), 0)

    def render_image(self, print_image: bool = False) -> list:
        """Render image pixel by pixel."""
        image = []

        for i in range(self.height):
            chunk = ''
            for j in range(self.width):
                pixels = [layer[i][j] for layer in self.layers]
                pixel = ([p for p in pixels if p != '2'] or ['2'])[0]
                chunk += pixel
            image.append(chunk)

        if print_image:
            self.print_image(image)

        return image

    def print_image(self, image: list):
        """Print image to stdout."""
        for chunk in image:
            for pixel in chunk:
                char = ' '
                if pixel == '1':
                    char = '█'
                elif pixel == '0':
                    char = '·'
                print(char, end='')
            print('')


if __name__ == '__main__':
    input_file = '2019/day8/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        data = f.readlines()[0].strip()
        decoder = SpaceImageFormatDecoder(data, width=25, height=6)
        print(f'Checksum: {decoder.get_checksum()}')  # 1340
        print('Rendered image:\n')
        decoder.render_image(print_image=True)  # LEJKC
