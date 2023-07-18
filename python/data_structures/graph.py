class Graph:
    def __init__(self):
        self.graph = {}

    def size(self):
        return len(self.graph)

    def add_node(self, value):
        node = Vertex(value)
        self.graph[node] = []
        return node

    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.graph or node2 not in self.graph:
            raise KeyError

        self.graph[node1].append(Edge(node2, weight))


    def get_neighbors(self, node):
        return self.graph[node]


    def get_nodes(self):
        return self.graph.keys()


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


