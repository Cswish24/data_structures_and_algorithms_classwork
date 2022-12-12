from disjointset import DisjointSet


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.vertices - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)


g = Graph(5)
g.addNode('a')
g.addNode('b')
g.addNode('c')
g.addNode('d')
g.addNode('e')

g.addEdge('a', 'b', 5)
g.addEdge('a', 'c', 13)
g.addEdge('a', 'e', 15)
g.addEdge('b', 'a', 5)
g.addEdge('b', 'c', 10)
g.addEdge('b', 'd', 8)
g.addEdge('c', 'a', 13)
g.addEdge('c', 'b', 10)
g.addEdge('c', 'e', 20)
g.addEdge('c', 'd', 6)
g.addEdge('d', 'b', 8)
g.addEdge('d', 'c', 6)
g.addEdge('e', 'a', 15)
g.addEdge('e', 'c', 20)

g.kruskalAlgo()
