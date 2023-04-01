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
        if self.head is None:
            return "NULL"
        current = self.head
        result = str(current.value)
        while current.next is not None:
            current = current.next
            result += f" ->{current.value}"
        return result

    def insert(self, value):
        if self.head is None:
            self.head= Node(value)
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)


class TargetError:
    pass
