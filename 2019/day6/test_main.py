from .main import OrbitMap

test_map = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""


def test_orbit_map_checkum():
    assert OrbitMap(test_map.split()).get_checksum() == 42


def test_orbit_map_transfers():
    result = test_map.split() + ['K)YOU', 'I)SAN']
    assert OrbitMap(result).get_orbital_transfers() == 4
