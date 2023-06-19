from collections import deque


def breadth_first_search(graph, start, condition) -> str:
    # Put initial nodes to queue
    queue = deque(graph[start])

    # Save all checked nodes to prevent cycles
    checked = set()

    while queue:
        left = queue.popleft()
        if left in checked:
            continue
        elif condition(left):
            return left
        else:
            new_nodes = graph[left]
            queue.extend(new_nodes)
            checked.add(left)

    return None


def test_breadth_first_search():
    graph = {}  # noqa
    graph["you"] = ["alice", "bob", "claire", "denis"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = ["dom"]
    graph["thom"] = ["gnom"]
    graph["jonny"] = []
    graph["denis"] = ["drom"]

    assert breadth_first_search(
        graph,
        start='you',
        condition=lambda name: name[-1] == 'm',
    ) == 'thom'


def test_breadth_first_search_cycle():
    graph = {
        'alice': ['bob'],
        'bob': ['alice'],
    }

    assert breadth_first_search(
        graph,
        start='alice',
        condition=lambda name: name == 'mark',
    ) is None
