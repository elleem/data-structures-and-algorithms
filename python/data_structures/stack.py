from data_structures.linked_list import Node

class Stack:
    """
    Create a Stack class that has a top property.
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
