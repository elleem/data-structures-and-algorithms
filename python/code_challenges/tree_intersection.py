from data_structures.binary_tree import BinaryTree


def tree_intersection(root1, root2):
    values_dict = {}
    queue = []
    queue.append(root1.root)
    while queue:
        node = queue[0]
        queue = queue[1:]
        values_dict[node.value] = True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    common_values = set()
    queue = []
    queue.append(root2.root)
    while queue:
        node = queue[0]
        queue = queue[1:]
        if node.value in values_dict:
            common_values.add(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return common_values
