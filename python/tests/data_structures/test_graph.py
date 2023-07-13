import pytest
from data_structures.graph import Graph, Vertex


def test_exists():
    assert Graph


# @pytest.mark.skip("TODO")
def test_add_node():

    graph = Graph()

    expected = "spam"  # a vertex's value that comes back

    actual = graph.add_node("spam").value

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_edge():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "banana"
    assert neighbors[0].weight == 5


# @pytest.mark.skip("TODO")
def test_bouquet():
    g = Graph()
    apple = g.add_node("apple")
    g.add_edge(apple, apple, 10)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "apple"
    assert neighbors[0].weight == 10


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    loner = Vertex("loner")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == "banana"

    assert neighbor_edge.weight == 44

#tests authored by Lauren after this point
def test_empty_graph_get_nodes():
    g = Graph()
    nodes = g.get_nodes()
    assert len(nodes) == 0


def test_get_neighbors_empty():
    g = Graph()
    node = g.add_node("node")
    neighbors = g.get_neighbors(node)
    assert len(neighbors) == 0


def test_add_edge_same_node():
    g = Graph()
    node = g.add_node("node")
    g.add_edge(node, node, 5)
    neighbors = g.get_neighbors(node)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "node"
    assert neighbors[0].weight == 5

def test_multiple_edges():
    g = Graph()
    node1 = g.add_node("node1")
    node2 = g.add_node("node2")
    node3 = g.add_node("node3")
    g.add_edge(node1, node2, 5)
    g.add_edge(node1, node3, 10)
    neighbors = g.get_neighbors(node1)
    expected_edges = {(node2, 5), (node3, 10)}

    assert len(neighbors) == len(expected_edges)
    assert {tuple((edge.vertex, edge.weight)) for edge in neighbors} == expected_edges

def test_add_edge_invalid_nodes():
    g = Graph()
    node1 = Vertex("node1")
    node2 = Vertex("node2")
    with pytest.raises(KeyError):
        g.add_edge(node1, node2, 5)


def test_add_nodes():
    g = Graph()
    node = g.add_node("node")
    assert isinstance(node, Vertex)
    assert len(g.graph) == 1
    assert len(g.get_nodes()) == 1

