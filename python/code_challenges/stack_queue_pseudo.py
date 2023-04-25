from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack_01 = Stack()
        self.stack_02 = Stack()


    def enqueue(self, value):

        while not self.stack_01.is_empty():
            self.stack_02.push(self.stack_01.pop())

        self.stack_01.push(value)

        while not self.stack_02.is_empty():
            self.stack_01.push(self.stack_02.pop())
    def dequeue(self):
        return self.stack_01.pop()

