import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []
    for bucket in hashtable._buckets:
        if bucket:
            actual.append(sorted(bucket))

    expected = [[("listen", "to me"), ("silent", True)], [("ahmad", 30)]]

    assert sorted(actual) == sorted(expected)

def test_set_and_get():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Yellow fruit")
    hashtable.set("orange", "Citrus fruit")

    assert hashtable.get("apple") == "Used for apple sauce"
    assert hashtable.get("banana") == "Yellow fruit"
    assert hashtable.get("orange") == "Citrus fruit"


def test_null_for_nonexistent_key():
    hashtable = Hashtable()

    assert hashtable.get("apple") is None
    assert hashtable.get("banana") is None
    assert hashtable.get("orange") is None


def test_unique_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Yellow fruit")
    hashtable.set("orange", "Citrus fruit")

    keys = hashtable.keys()

    assert len(keys) == 3
    assert "apple" in keys
    assert "banana" in keys
    assert "orange" in keys


def test_collision_handling():
    hashtable = Hashtable(4)  # Small size to induce collisions
    hashtable.set("ahmad", 30)
    hashtable.set("mehdi", 25)

    # Both keys should be stored in the same bucket
    bucket = hashtable._buckets[hashtable._hash("ahmad")]
    assert ("ahmad", 30) in bucket
    assert ("mehdi", 25) in bucket


def test_retrieve_value_from_collision_bucket():
    hashtable = Hashtable(4)  # Small size to induce collisions
    hashtable.set("ahmad", 30)
    hashtable.set("mehdi", 25)

    # Retrieve values from the collision bucket
    value_ahmad = hashtable.get("ahmad")
    value_mehdi = hashtable.get("mehdi")

    assert value_ahmad == 30
    assert value_mehdi == 25


def test_hash_range():
    hashtable = Hashtable(100)
    key = "apple"
    index = hashtable._hash(key)

    assert index >= 0 and index < 100
