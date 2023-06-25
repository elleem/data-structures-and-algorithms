from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(tree):
    if tree.root is None:
        return None

    new_node = Node(fizz_buzz_helper(tree.root.value))

    for child in tree.root.children:
        new_child = fizz_buzz_tree(KaryTree(child))
        new_node.children.append(new_child.root)

    return KaryTree(new_node)

def fizz_buzz_helper(value):
    if value % 15 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)


