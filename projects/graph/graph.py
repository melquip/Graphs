"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check that v1 and v2 exist in the vertices dictionary
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 to the vertices at v1
            self.vertices[v1].add(v2)
            # # add v1 to the vertices at v2 bidirectional or undirected
            # self.vertices[v2].add(v1)
        # otherwise
        else:
            # raise and exception and give an error
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, sv):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        q = Queue()
        q.enqueue(sv)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        return visited

    def dft(self, sv):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(sv)
        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive_h(self, v, visited, stack):
        if stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.vertices[v]:
                    stack.push(next_vertex)
            self.dft_recursive_h(v, visited, stack)
        else:
            return False

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        self.dft_recursive_h(starting_vertex, visited, s)
        return visited

    def bfs(self, sv, dv):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        Create an empty queue and enqueue A PATH TO the starting vertex ID
        Create a Set to store visited vertices
        While the queue is not empty...
            Dequeue the first PATH eg -> [a, b, c, r, g]
            Grab the last vertex from the PATH
            If that vertex has not been visited...
                CHECK IF IT'S THE TARGET
                    IF SO, RETURN PATH

                Mark it as visited...
                Then add A PATH TO its neighbors to the back of the queue
                COPY THE PATH
                APPEND THE NEIGHOR TO THE BACK
        """
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

                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

                    if neighbor == dv:
                        return new_path

                visited.add(vertex)
        
        raise ValueError(f'This destination vertex is not connected to the starting vertex.')

    def dfs(self, sv, dv):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = Stack()
        stack.push([sv])
        
        if sv == dv:
            return [sv, dv]

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == dv:
                    return path

                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.push(new_path)

                    if neighbor == dv:
                        return new_path

                visited.add(vertex)
        
        raise ValueError(f'This destination vertex is not connected to the starting vertex.')

    def dfs_recursive(self, sv, dv, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = [sv]
        if sv == dv:
            return path
        neighbors = self.get_neighbors(sv)
        for neighbor in neighbors - set(path):
            findPath = self.dfs_recursive(neighbor, dv, path + [neighbor])
            if findPath is not None:
                return findPath
        
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
