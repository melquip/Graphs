from collections import defaultdict
from util import Queue, Stack

def earliest_ancestor(ancestors, sv):
    graph = defaultdict(set)
    for (parent, child) in ancestors:
        if not graph[parent]:
            graph[parent] = set()
        graph[parent].add(child)
    return dfs(graph, sv, ancestors)

# second pass solution
def dfs(graph, sv, ancestors):
    visited = set()
    stack = Stack()
    stack.push([sv])
    while stack.size() > 0:
        path = stack.pop()
        nodes = set(path) - visited
        for vertex in nodes:
            parents = [parent for (parent, child) in ancestors if child == vertex]
            if len(parents) == 0:
                return -1 if path[-1] == sv else path[-1]
            new_path = list(path)
            new_path.append(min(parents))
            stack.push(new_path)
            visited.add(vertex)
    
# first pass solution
def bfs(graph, sv, ancestors):
    visited = set()
    queue = Queue()
    queue.enqueue([sv])
    while queue.size() > 0:
        path = queue.dequeue()
        nodes = set(path) - visited
        for vertex in nodes:
            parents = [parent for (parent, child) in ancestors if child == vertex]
            if len(parents) != 0:
                parents = [min(parents)]
            parentsOfParents = [parent for (parent, child) in ancestors if child in parents]
            if len(parentsOfParents) == 0:
                return -1 if len(parents) == 0 else min(parents)
            for parent in parents:   
                new_path = list(path)
                new_path.append(parent)
                queue.enqueue(new_path)
            visited.add(vertex)

if __name__ == '__main__':
    '''
    {
        10: {1}
        1: {3}, 
        2: {3}, 
        4: {8, 5}, 
        3: {6}, 
        5: {6, 7}, 
        11: {8}, 
        8: {9}, 
    }
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
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
