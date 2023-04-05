import pytest
from data_structures.linked_list import LinkedList, TargetError

# Can successfully add multiple nodes to the end of a linked list
def test_append_mult_nodes_to_end():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)

    assert linked_list.head.value == 5
    assert linked_list.head.next.value == 1
    assert linked_list.head.next.next.value == 3
    assert linked_list.head.next.next.next.value == 2
    assert linked_list.head.next.next.next.next is None

#Can successfully add a node to the end of the linked list
def test_append_one():
    linked_list = LinkedList()
    linked_list.append(1)


    assert linked_list.head.value == 1
    assert linked_list.head.next is None

# @pytest.mark.skip("TODO")
def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"


# @pytest.mark.skip("TODO")
def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"

# Can successfully insert a node before a node located i the middle of a linked list
# Can successfully insert a node before the first node of a linked list
@pytest.mark.skip("TODO")
def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")
