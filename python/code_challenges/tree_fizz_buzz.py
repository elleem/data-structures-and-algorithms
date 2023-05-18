from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(tree):
    if not tree.root:
        return None

    def fizz_buzz_helper(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            transformed_value = "FizzBuzz"
        elif node.value % 3 == 0:
            transformed_value = "Fizz"
        elif node.value % 5 == 0:
            transformed_value = "Buzz"
        else:
            transformed_value = str(node.value)

        tranformed_node = Node(transformed_value)
        for child in node.children:
            transformed_child = fizz_buzz_helper(child)
            tranformed_node.children.append(transformed_child)
        return tranformed_node


    transformed_root = fizz_buzz_helper(tree.root)
    transformed_tree = KaryTree(transformed_root)

    return transformed_tree
