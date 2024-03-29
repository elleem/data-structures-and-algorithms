class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    A class representing a binary tree.
    Attributes:
        value of the current node
        The left child of the current node.
        The right child of the current node.

    Methods: for pre order, in order, and post order, which implement as top down, left to right, and bottom up.
    """

    def __init__(self):
        self.root = None


    #passing in two params, root of the tree to be traversed and an empty list to hold values visited during the traversal
    def pre_order(self, root = None, node=None):
        # initialize empty list
        if node is None:
            node = []
        # checks for empty root
        if root is None:
            root = self.root
        # add the value of current node to list of nodes visited during traversal
        if root:
            node.append(root.value)
            if root.left:
                self.pre_order(root.left, node)
            if root.right:
                self.pre_order(root.right, node)
        return node


    def in_order(self, root=None, node=None):
        if node is None:
            node = []
        if root is  None:
            root = self.root
        if root:
            if root.left:
                self.in_order(root.left,node)
            node.append(root.value)
            if root.right:
                self.in_order(root.right,node)
        return node


    def post_order(self, root=None, node=None):
        if node is None:
            node = []
        if root is  None:
            root = self.root
        if root:
            if root.left:
                self.post_order(root.left,node)
            if root.right:
                self.post_order(root.right,node)
            node.append(root.value)
        return node

    def find_maximum_value(self):
        max_value = float('-inf')
        nodes = self.in_order()

        for node_value in nodes:
            if node_value > max_value:
                max_value = node_value

        return max_value
