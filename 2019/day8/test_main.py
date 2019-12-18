from .main import SpaceImageFormatDecoder


def test_layers_amount():
    """Test `get_layers`."""
    decoder = SpaceImageFormatDecoder('123456789012', width=3, height=2)
    assert len(decoder.layers) == 2
    assert decoder.layers[0] == ['123', '456']
    assert decoder.layers[1] == ['789', '012']


def test_count_digits_on_layer():
    """Test `count_digits`."""
    decoder = SpaceImageFormatDecoder('120400789012', width=3, height=2)
    assert decoder.count_digits(0, layer=decoder.layers[0]) == 3
    assert decoder.count_digits(1, layer=decoder.layers[0]) == 1
    assert decoder.count_digits(9, layer=decoder.layers[0]) == 0
    assert decoder.count_digits(0, layer=decoder.layers[1]) == 1


def test_render_image():
    """Test `render_image`."""
    decoder = SpaceImageFormatDecoder('0222112222120000', width=2, height=2)
    assert decoder.render_image() == ['01', '10']
