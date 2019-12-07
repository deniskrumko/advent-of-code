class OrbitMap:

    def __init__(self, orbit_map: list):
        """Initialize class instance."""
        self.orbit_map: list = orbit_map
        self.orbit_system: dict = {}
        self.build_orbit_system()

    def build_orbit_system(self):
        """Build orbit system as dict of parent-child relations."""
        for value in self.orbit_map:
            parent, child = value.strip().split(')')
            self.orbit_system.setdefault(parent, None)
            self.orbit_system[child] = parent

    def get_checksum(self) -> int:
        """Get checksum for current ``OrbitMap``."""
        return sum(self.get_node_checksum(key) for key in self.orbit_system)

    def get_node_checksum(self, key, result=0):
        """Get checksum of separate node (planet)."""
        if self.orbit_system[key] is None:
            return result

        key = self.orbit_system[key]
        return self.get_node_checksum(key, result + 1)

    def get_all_parents(self, child, parents=None):
        """Get all parent planets for current child planet."""
        parents = parents or []
        current_parent = self.orbit_system[child]
        if current_parent is None:
            return parents

        parents.append(current_parent)
        return self.get_all_parents(child=current_parent, parents=parents)

    def get_orbital_transfers(self) -> int:
        """Get orbital transfers between you and Santa 🎅."""
        you_parents = self.get_all_parents(child='YOU')
        san_parents = self.get_all_parents(child='SAN')
        return len(set(you_parents) ^ set(san_parents))


if __name__ == '__main__':
    input_file = '2019/day6/input.txt'
    print(f'Input file: {input_file}')

    with open(input_file, 'r') as f:
        orbit = OrbitMap(orbit_map=f.readlines())
        print(f'Checksum: {orbit.get_checksum()}')  # 387356
        print(f'Orbital transfers: {orbit.get_orbital_transfers()}')  # 532
