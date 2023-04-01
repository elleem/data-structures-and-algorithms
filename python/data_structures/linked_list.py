class Node:
    #create a node class with value and pointer to the next node
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
create a LinkedList class, include head, upon instantiation an empty LinkedList is created
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        #Returns: a string representing all the values in the Linked List, formatted as: "{a} ->"
        if self.head is None:
            return "NULL"
        current = self.head
        result = f"{{ {current.value} }}"
        while current.next is not None:
            current = current.next
            result += f" -> {{ {current.value} }}"
        result += " -> NULL"
        return result

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def includes(self, value):
        #Indicates whether that value exists as a Node’s value somewhere within the list. returns boolean
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

class TargetError:
    pass
#   raise TargetError
