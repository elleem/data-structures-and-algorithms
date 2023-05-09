import pytest
from data_structures.binary_search_tree import BinarySearchTree


def test_exists():
    assert BinarySearchTree


# @pytest.mark.skip("TODO")
def test_instantiate_empty():
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_to_empty():
    tree = BinarySearchTree()
    tree.add("apples")
    actual = tree.root.value
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_left():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    actual = tree.root.left.value
    expected = 5
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_right():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)
    actual = tree.root.right.value
    expected = 15
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_deeper(tree):
    tree.add(25)
    actual = tree.root.right.right.value
    expected = 25
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_contains(tree):
    actual = tree.contains(15)
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_contains_deeper(tree):
    actual = tree.contains(5)
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_not_contains(tree):
    actual = tree.contains(100)
    expected = False
    assert actual == expected


@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    return tree

# tests below authored by Lauren


def test_contains_false(tree):
    tree = BinarySearchTree()
    tree.add("apples")
    assert tree.contains('z') == False

def test_contains_true(tree):
    tree = BinarySearchTree()
    tree.add('d')
    assert tree.contains('d') == True


def test_add_children_to_node():
    tree = BinarySearchTree()
    tree.add(4)
    tree.add(2)
    tree.add(6)
    tree.add(1)
    tree.add(3)
    tree.add(5)
    tree.add(7)
    assert tree.root.value == 4
    assert tree.root.left.value == 2
    assert tree.root.right.value == 6
    assert tree.root.left.left.value == 1
    assert tree.root.left.right.value == 3
    assert tree.root.right.left.value == 5
    assert tree.root.right.right.value == 7

def test_add_existing_node():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(10)
    assert tree.root.left is None
    assert tree.root.right is not None


def test_contains_empty():
    tree = BinarySearchTree()
    assert tree.contains(10) == False

def test_contains_single_node():
    tree = BinarySearchTree()
    tree.add(10)
    assert tree.contains(10) == True

def test_contains_multiple_nodes():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(2)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    assert tree.contains(10) == True
    assert tree.contains(5) == True
    assert tree.contains(15) == True
    assert tree.contains(2) == True
    assert tree.contains(7) == True
    assert tree.contains(12) == True
    assert tree.contains(20) == True
    assert tree.contains(11) == False
    assert tree.contains(6) == False
