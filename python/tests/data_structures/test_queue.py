import pytest
from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError


def test_exists():
    assert Queue


# @pytest.mark.skip("TODO")
def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()


# @pytest.mark.skip("TODO")
def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


# @pytest.mark.skip("TODO")
def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

# the following tests authored by Lauren

def test_peek_singular():
    q = Queue()
    q.enqueue("apple")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_enqueue_integers():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    actual = q.front.value
    expected = 1
    assert actual == expected

def test_enqueue_dequeue_loop():
    q = Queue()

    # enqueue elements onto the queue
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    # dequeue elements off the queue in reverse order
    actual = q.dequeue()
    expected = 0
    assert actual == expected

    actual = q.dequeue()
    expected = 1
    assert actual == expected

    actual = q.dequeue()
    expected = 2
    assert actual == expected

    actual = q.dequeue()
    expected = 3
    assert actual == expected

    actual = q.dequeue()
    expected = 4
    assert actual == expected

    # check if queue is empty
    assert q.is_empty()

def test_enqueue_dequeue_different_data_types():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2.5)
    q.enqueue("string")

    actual =  q.dequeue()
    expected = 1
    assert actual == expected

    actual = q.dequeue()
    expected = 2.5
    assert actual == expected

    actual = q.dequeue()
    expected = "string"
    assert actual == expected

    assert q.is_empty()


def test_enqueue_large_number_of_elements():
    q = Queue()
    for i in range(100000):
        q.enqueue(i)
    actual = q.rear.value
    expected = 99999
    assert actual == expected


def test_enqueue_dequeue_same_element():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected

def test_enqueue_dequeue_mix():
    q = Queue()
    q.enqueue("apple")
    q.enqueue(123)
    q.enqueue([1,2,3])
    q.enqueue({"name": "Lauren", "status": "student"})
    actual = q.dequeue()
    expected = "apple"
    assert actual ==expected
    actual = q.dequeue()
    expected = 123
    assert actual ==expected
    actual = q.dequeue()
    expected = [1,2,3]
    assert actual ==expected
    actual = q.dequeue()
    expected = {"name": "Lauren", "status": "student"}
    assert actual ==expected

    assert q.is_empty()

def test_none():
    q = Queue()
    q.enqueue (None)
    actual = q.rear.value
    expected = None
    assert actual == expected

def test_enqueue_dequeue_random():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    # randomly dequeue elements off the stack
    dequeue = []
    while not q.is_empty():
        element = q.dequeue()
        dequeue.append(element)

    # check if dequeued elements are in reverse order
    expected = [1,2,3,4]
    assert dequeue == expected

def test_enqueue_dequeue_large_number_of_elements():
    q = Queue()
    for i in range(100000):
        q.enqueue(i)

    for i in range(100000):
        q.dequeue()

    assert q.is_empty()
    assert q.rear is None
