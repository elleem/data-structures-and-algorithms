from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs_queue = Queue()
        self.cats_queue = Queue()


    def enqueue(self, animal):
        if animal.name == "dog":
            self.dogs_queue.enqueue(animal)
        if animal.name == "cat":
            self.cats_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog":
            return self.dogs_queue.dequeue()
        elif pref == "cat":
            return self.cats_queue.dequeue()

        return None


class Dog:
    def __init__(self, name ="dog"):
        self.name = name
        self.next = next


class Cat:
    def __init__(self, name ="cat"):
        self.name = name
        self.next = next
