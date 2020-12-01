class PipeVillage(object):
    """Docstring"""

    def __init__(self, path):
        """Custom `__init__` method."""
        self.tree = {}
        self.visited = []
        with open(path, 'r') as f:
            for line in f:
                node, links = [
                    link.strip().replace('\n', '') for link in line.split('<->')
                ]
                links = [int(link) for link in links.split(',')]

                self.tree[int(node)] = links

    def find_connection(self, root_node, to, visited):
        links = self.tree[root_node]

        if root_node == to or to in links:
            return True

        if root_node in links:
            return False

        visited.append(root_node)

        for link in self.tree[root_node]:
            if link in visited:
                continue

            connect = self.find_connection(link, to, visited)
            if connect:
                return True

        return False

    def get_group_size(self, start_node):
        return len(self.walk_tree(start_node, visited=[]))

    def walk_tree(self, node, visited):
        if node in visited:
            return

        visited.append(node)

        for link in self.tree[node]:
            self.walk_tree(link, visited)

        return visited

    def get_groups_amount(self):
        in_groups = []
        groups_amount = 0
        for node in self.tree.keys():
            if node in in_groups:
                continue

            in_groups += self.walk_tree(node, visited=[])
            groups_amount += 1

        return groups_amount


if __name__ == '__main__':
    test_pv = PipeVillage('day12/test_input.txt')

    assert test_pv.get_group_size(0) == 6
    assert test_pv.get_groups_amount() == 2

    pv = PipeVillage('day12/input.txt')

    print(pv.get_group_size(0))
    print(pv.get_groups_amount())
