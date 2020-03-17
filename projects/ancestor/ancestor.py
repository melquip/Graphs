from collections import defaultdict
from util import Queue

def earliest_ancestor(ancestors, sv):
    graph = defaultdict(set)
    #parents = []
    for (parent, child) in ancestors:
        if not graph[parent]:
            graph[parent] = set()
        graph[parent].add(child)
        #parents.append(parent)
    print('\n\nstarting', sv)
    return bfs(graph, sv, ancestors)

def bfs(graph, sv, ancestors):
    visited = set()
    queue = Queue()
    queue.enqueue([sv])
    while queue.size() > 0:
        path = queue.dequeue()
        nodes = path - list(visited)
        print('vertex?', nodes)
        for vertex in nodes:
            parents = [parent for (parent, child) in ancestors if child == vertex]
            print('parents?', parents)
            parentsOfParents = [parent for (parent, child) in ancestors if child in parents]
            print('parentsOfParents?', parentsOfParents, len(parentsOfParents))
            if len(parentsOfParents) == 0:
                return -1 if len(parents) == 0 else min(parents)
            for parent in parents:   
                visited.add(parent)                 
                new_path = list(path)
                new_path.append(parent)
                # if len(parentsOfParents) == 1:
                #     new_path.append(parentsOfParents[0])
                queue.enqueue(new_path)
            visited.add(vertex)
    
    # raise ValueError(f'This destination vertex is not connected to the starting vertex.')



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
