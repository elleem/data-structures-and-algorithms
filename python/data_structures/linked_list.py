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
        #initialize a variable named current, set to head
        current = self.head
        #this allows you to literally match the format of the test
        result = f"{{ {current.value} }}"
        #start a while loop, choose b/n current or current.next node
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

    def append(self, value):
        #adds a new node with the given value to the end of the list
        new_node = Node(value)
        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node



    def insert_before(self, value, new_value):
    # adds a new node with the given new value immediately before the first node that has the value specified

        if self.head is not None and self.head.value == value:
            self.insert(new_value)
            return

        current = self.head
    #while the node value is not null and the current next value, doesn't equal the target value, the traverse
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is None:
            raise ValueError(f"Value {value} not found in linked list")

        new_node = Node(new_value)
        new_node.next = current.next
        current.next= new_node
    #
    # def insert_after(self, value, new_value):
    #adds a new node with the given new value immediately after the first node that has the value specified
    #     pass

class TargetError:
    pass
#   raise TargetError
