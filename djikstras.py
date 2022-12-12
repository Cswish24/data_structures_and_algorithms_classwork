# class for djikstras

import heapq


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float('inf')

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, other_vertex):
        edge = Edge(self, other_vertex, weight)
        self.neighbors.append(edge)


class Djikstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited == True:
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start
                end = edge.end
                new_distance = actual_vertex.min_distance + edge.weight
                if new_distance < end.min_distance:
                    end.min_distance = new_distance
                    end.predecessor = start
                    heapq.heappush(self.heap, end)

            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f'shortest path = {vertex.min_distance}')
        actual_vertex = vertex
        while actual_vertex:
            print(f'{actual_vertex.name}', end=' ')
            actual_vertex = actual_vertex.predecessor


nodea = Node('a')
nodeb = Node('b')
nodec = Node('c')
noded = Node('d')
nodee = Node('e')
nodef = Node('f')
nodeg = Node('g')
nodeh = Node('h')

nodea.add_edge(6, nodeb)
nodea.add_edge(10, nodec)
nodea.add_edge(9, noded)

nodeb.add_edge(5, noded)
nodeb.add_edge(16, nodee)
nodeb.add_edge(13, nodef)

nodec.add_edge(6, noded)
nodec.add_edge(5, nodeh)
nodec.add_edge(21, nodeg)

noded.add_edge(8, nodef)
noded.add_edge(7, nodeh)

nodee.add_edge(10, nodeg)

nodef.add_edge(4, nodee)
nodef.add_edge(12, nodeg)

nodeh.add_edge(2, nodef)
nodeh.add_edge(14, nodeg)

algorithm = Djikstra()
algorithm.calculate(nodea)
algorithm.get_shortest_path(nodeg)
