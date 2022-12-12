from queue import Queue
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for item in self.adjacency_list[vertex]:
                self.adjacency_list[item].remove(vertex)
            self.adjacency_list.pop(vertex)
            return True
        return False

    def bfs(self, start):
        queue = Queue()
        visited = [start]
        queue.put(start)
        while not queue.empty():
            vertice = queue.get()
            for other_vertice in self.adjacency_list[vertice]:
                if other_vertice not in visited:
                    queue.put(other_vertice)
                    visited.append(other_vertice)
            print(vertice)

    def dfs(self, start):
        stack = [start]
        visited = [start]
        while stack:
            vertice = stack.pop()
            for other_vertice in self.adjacency_list[vertice]:
                if other_vertice not in visited:
                    stack.append(other_vertice)
                    visited.append(other_vertice)
            print(vertice)

    def __str__(self):
        for key, values in self.adjacency_list.items():
            print(f'{key}: {values}')
        return

    def print_graph(self):
        for key, values in self.adjacency_list.items():
            print(f'{key}: {values}')
        return


graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('d', 'b')
graph.add_edge('c', 'd')
graph.add_edge('c', 'e')
graph.add_edge('e', 'f')
graph.add_edge('a', 'f')
# print(graph.adjacency_list)
graph.print_graph()
print('---------------')
graph.bfs('a')
print('------------')
graph.dfs('a')
# graph.remove_vertex('a')
# graph.print_graph()
# graph.remove_edge('a', 'b')
# graph.print_graph()


class DirectedGraph():
    def __init__(self, numberofvertices):
        self.graph = defaultdict(list)
        self.numberofvertices = numberofvertices

    def add_vertice(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex, vertex2):
        if vertex in self.graph.keys() and vertex2 in self.graph.keys():
            self.graph[vertex].append(vertex2)

    def print_graph(self):
        for key, values in self.adjacency_list.items():
            print(f'{key}: {values}')
        return

    def topological_sort_helper(self, visited, stack, point):
        visited.append(point)

        for j in self.graph[point]:
            if j not in visited:
                visited.append(j)
                self.topological_sort_helper(visited, stack, j)
        stack.insert(0, point)

    def topological_sort(self):
        visited = []
        stack = []
        for i in self.graph:
            if i not in visited:
                self.topological_sort_helper(visited, stack, i)
        return stack

    def breadth_first_ssp(self, start, end):
        queue = Queue()
        queue.put([start])
        while not queue.empty():
            vertices = queue.get()
            node = vertices[-1]
            if node == end:
                return vertices
            for other_vertice in self.graph.get(node, []):
                new_path = list(vertices)
                new_path.append(other_vertice)
                queue.put(new_path)


print('----------------')
print('topological sort')
dgraph = DirectedGraph(0)

dgraph.add_vertice('a')
dgraph.add_vertice('b')
dgraph.add_vertice('c')
dgraph.add_vertice('d')
dgraph.add_vertice('e')
dgraph.add_vertice('f')
dgraph.add_vertice('g')
dgraph.add_vertice('h')
dgraph.add_edge('a', 'c')
dgraph.add_edge('b', 'c')
dgraph.add_edge('a', 'd')
dgraph.add_edge('d', 'e')
dgraph.add_edge('c', 'e')
dgraph.add_edge('d', 'f')
dgraph.add_edge('e', 'g')
dgraph.add_edge('g', 'h')
sorted = dgraph.topological_sort()
print(sorted)
print('----------------------')
print('breadth first shortest path solution')
dgraph.add_edge('f', 'e')
dgraph.add_edge('c', 'g')
shortest_bfs = dgraph.breadth_first_ssp('a', 'h')
print(shortest_bfs)
