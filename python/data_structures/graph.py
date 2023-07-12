class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        node = Vertex(value)
        self.graph[node] = []
        return node

    def add_edge(self,node1,node2,weight):
        self.add_node(node1)
        self.add_node(node2)

        self.graph[node1].append([node2, weight])
        self.graph[node2].append([node1, weight])

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self,vertex):
        if vertex in self.graph:
            neighbors = []
            for neighbor, weight in self.graph[vertex]:
                neighbor_vertex = Vertex(neighbor.value)
                neighbor_vertex.weight = weight
                neighbors.append(neighbor_vertex)
            return neighbors
        else:
            return []

    def size(self):
        return len(self.graph)

    def get_nodes(self):
        return self.graph

class Vertex:
    def __init__(self, value):
        self.value = value
