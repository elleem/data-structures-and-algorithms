import pytest
from code_challenges.linked_list_zip import zip_lists
from data_structures.linked_list import LinkedList


def test_exists():
    assert zip_lists


# @pytest.mark.skip("TODO")
def test_even_length():
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1, "a", 2, "b", 3, "c"]):
        expected.insert(value)

    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_a_shorter():
    list_a = LinkedList()
    for value in reversed([1, 2]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1, "a", 2, "b", "c"]):
        expected.insert(value)

    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_b_shorter():
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1, "a", 2, "b", 3]):
        expected.insert(value)

    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_a_empty():
    list_a = LinkedList()
    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed(["a", "b", "c"]):
        expected.insert(value)
    assert str(actual) == str(expected)


# @pytest.mark.skip("TODO")
def test_b_empty():
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)
    list_b = LinkedList()
    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1, 2, 3]):
        expected.insert(value)
    assert str(actual) == str(expected)

# tests after this note authored by Lauren

def test_single_element_lists():
    list_a = LinkedList()
    for value in reversed([1]):
        list_a.insert(value)
    list_b = LinkedList()
    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1]):
        expected.insert(value)
    assert str(actual) == str(expected)

def test_both_empty():
    list_a = LinkedList()
    list_b = LinkedList()

    actual = zip_lists(list_a, list_b)

    expected = LinkedList()
    assert str(actual) == str(expected)

def test_repeated_lists():
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed([1,2,3]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1, 1, 2, 2, 3, 3]):
        expected.insert(value)

    assert str(actual) == str(expected)

def test_repeated_items_in_list():
    list_a = LinkedList()
    for value in reversed([1, 1, 1]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed([1,2,3]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed([1, 1, 1, 2, 1, 3]):
        expected.insert(value)

    assert str(actual) == str(expected)


def test_for_a_fun_message():
    list_a = LinkedList()
    for value in reversed(["Lauren", "enrolled", "Code"]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["is", "at", "Fellows!"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = LinkedList()
    for value in reversed(["Lauren", "is", "enrolled", "at", "Code", "Fellows!"]):
        expected.insert(value)

    assert str(actual) == str(expected)


