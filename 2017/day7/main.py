class Node:

    def __init__(self, weight=None, parent=None):
        self.weight = weight
        self.parent = parent


def tower_weight(root_key, nodes):
    sum_weight = 0

    child_nodes = get_child_nodes(nodes, root_key)

    if not child_nodes:
        return nodes[root_key].weight

    for key in child_nodes:
        sum_weight += tower_weight(key, nodes)

    return sum_weight + nodes[root_key].weight


def get_child_nodes(nodes, root):
    result = []
    for key, node in nodes.items():
        if node.parent == root:
            result.append(key)

    return result


def get_tower_bottom(nodes):
    for node_key in nodes.keys():
        current_node = node_key
        while True:
            if not nodes[current_node].parent:
                return current_node

            current_node = nodes[current_node].parent


def get_nodes_dict(path):
    nodes = {}

    with open(path, 'r') as f:
        puzzle = f.readlines()

    for line in puzzle:
        parts = line.split('->')

        root_key, weight = parts[0].split()
        weight = int(weight.replace('(', '').replace(')', ''))
        leaves = []

        if len(parts) > 1:
            leaves = [p.strip() for p in parts[1].replace('\n', '').split(',')]

        nodes.setdefault(root_key, Node(weight=weight, parent=None))

        nodes[root_key].weight = weight

        for key in leaves:
            nodes.setdefault(key, Node(weight=None, parent=root_key))
            nodes[key].parent = root_key

    return nodes


def get_fat(nodes, root_key, should_weight=0):
    child_nodes = get_child_nodes(nodes, root_key)

    weights = []

    for key in child_nodes:
        weights.append(tower_weight(key, nodes))

    if len(set(weights)) == 1:
        return should_weight

    different_node = None
    different_node_weight = None
    normal_weight = None

    for index, weight in enumerate(weights):
        if weights.count(weight) == 1:
            different_node = child_nodes[index]
            different_node_weight = weight
        else:
            normal_weight = weight

    overweight = different_node_weight - normal_weight

    should_weight = nodes[different_node].weight - overweight

    return get_fat(nodes, different_node, should_weight)


def main():
    nodes = get_nodes_dict(path='day7/input.txt')

    # nodes['vwkkml'].weight = 148784

    bottom = get_tower_bottom(nodes)

    print('bottom node is {}'.format(bottom))

    print(get_fat(nodes, bottom))


if __name__ == '__main__':
    main()
