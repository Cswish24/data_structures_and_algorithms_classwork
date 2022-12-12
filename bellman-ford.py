

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, start, end, weight):
        self.graph.append([start, end, weight])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, distance):
        print('Vertex distance')
        for key, value in distance.items():
            print(' ' + key, ' :    ', value)

    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.vertices-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
            self.print_solution(dist)
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print('Graph contains negative cylcle')
                self.print_solution(dist)
                return

        self.print_solution(dist)


g = Graph(4)

g.addNode("a")
g.addNode("b")
g.addNode("c")
g.addNode("d")
g.addNode("e")

g.add_edge("a", "c", 6)
g.add_edge("a", "d", -6)
g.add_edge("b", "a", 3)
g.add_edge("c", "d", 1)
g.add_edge("d", "c", 2)
g.add_edge("d", "b", 1)
g.add_edge("e", "b", 4)
g.add_edge("e", "d", 2)

g.bellmanFord('e')
