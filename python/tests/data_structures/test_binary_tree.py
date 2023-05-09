import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree

#the tests below authored by Lauren

def test_empty_root_pre_order():
    tree = BinaryTree()
    actual = tree.pre_order()
    expected = []
    assert actual == expected


def test_in_order_single_node():
    tree = BinaryTree()
    tree.root = Node(5)
    assert tree.pre_order() == [5]


def test_post_order_multiple_nodes():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(7)
    assert tree.post_order() == [3,7,5]


def test_pre_order_traversal(tree):
    expected = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    assert tree.pre_order()==expected

def test_post_order_traversal(tree):
    expected = ['d','e', 'b', 'f', 'g', 'c', 'a']
    assert tree.post_order()==expected


def test_in_order_traversal(tree):
    expected = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
    assert tree.in_order()==expected
