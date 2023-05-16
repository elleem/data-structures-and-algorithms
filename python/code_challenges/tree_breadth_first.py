from data_structures.binary_tree import BinaryTree


def breadth_first(tree):

    if tree.root is None:
        return []
    visited_nodes_list = []

    queue = [tree.root]

    while len(queue) > 0:
        node = queue.pop(0)
        visited_nodes_list.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


    return visited_nodes_list
