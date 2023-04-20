import pytest
from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError


def test_exists():
    assert Stack


# @pytest.mark.skip("TODO")
def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


# @pytest.mark.skip("TODO")
def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"


# the following tests authored by Lauren

def test_peek_singular():
    s = Stack()
    s.push("apple")
    actual = s.peek()
    expected = "apple"
    assert actual == expected


def test_push_integers():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    actual = s.top.value
    expected = 3
    assert actual == expected

def test_push_pop_loop():
    s = Stack()

    # push elements onto the stack
    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    # pop elements off the stack in reverse order
    actual = s.pop()
    expected = 4
    assert actual == expected

    actual = s.pop()
    expected = 3
    assert actual == expected

    actual = s.pop()
    expected = 2
    assert actual == expected

    actual = s.pop()
    expected = 1
    assert actual == expected

    actual = s.pop()
    expected = 0
    assert actual == expected

    # check if stack is empty
    assert s.is_empty()

