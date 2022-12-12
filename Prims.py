import sys


class Graph:
    def __init__(self, vertex_num, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertex_num = vertex_num
        self.MST = []

    def print_solution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def prims_algo(self):
        visited = [0]*self.vertex_num
        edge_num = 0
        visited[0] = True
        while edge_num < self.vertex_num - 1:
            min = sys.maxsize
            for i in range(self.vertex_num):
                if visited[i]:
                    for j in range(self.vertex_num):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edge_num += 1
        self.print_solution()


edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]

nodes = ['a', 'b', 'c', 'd', 'e']
g = Graph(5, edges, nodes)
g.prims_algo()
