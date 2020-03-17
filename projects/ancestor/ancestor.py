from collections import defaultdict
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = defaultdict(set)
    for (parent, child) in ancestors:
        if not graph[parent]:
            graph[parent] = set()
        graph[parent].add(child)

    print(graph)


def bfs(graph, sv, dv):
    visited = set()
    queue = Queue()
    queue.enqueue([sv])
    
    if sv == dv:
        return [sv, dv]

    while queue.size() > 0:
        visited = set()
        path = queue.dequeue()
        vertex = path[-1]
        if vertex not in visited:
            if vertex == dv:
                return path

            neighbors = graph[vertex]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.enqueue(new_path)

                if neighbor == dv:
                    return new_path

            visited.add(vertex)
    
    raise ValueError(f'This destination vertex is not connected to the starting vertex.')



if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 1), 10)
    print(earliest_ancestor(test_ancestors, 2), -1)
    print(earliest_ancestor(test_ancestors, 3), 10)
    print(earliest_ancestor(test_ancestors, 4), -1)
    print(earliest_ancestor(test_ancestors, 5), 4)
    print(earliest_ancestor(test_ancestors, 6), 10)
    print(earliest_ancestor(test_ancestors, 7), 4)
    print(earliest_ancestor(test_ancestors, 8), 4)
    print(earliest_ancestor(test_ancestors, 9), 4)
    print(earliest_ancestor(test_ancestors, 10), -1)
    print(earliest_ancestor(test_ancestors, 11), -1)
