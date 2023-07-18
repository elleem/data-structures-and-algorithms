import pytest
from code_challenges.three_odds import three_consecutive_odds

def test_exists():
    assert three_consecutive_odds

def test_empty_list():
    expected = None
    actual = three_consecutive_odds([])
    assert actual == expected

def test_less_than_three_numbers():
    expected = None
    actual = three_consecutive_odds([1,2])
    assert actual == expected

def test_consecutive_odds_at_beginning():
    expected = True
    actual = three_consecutive_odds([3, 5, 7, 2, 4])
    assert actual == expected

def test_consecutive_odds_at_end():
    expected = True
    actual = three_consecutive_odds([2, 4, 6, 3, 5, 7])
    assert actual == expected

def test_consecutive_odds_in_middle():
    expected = True
    actual = three_consecutive_odds([2, 3, 5, 7, 9, 4, 6])
    assert actual == expected

def test_consecutive_odds_same_number():
    expected = True
    actual = three_consecutive_odds([3, 3, 3, 2, 4, 6])
    assert actual == expected

def test_consecutive_odds_diff_numbers():
    expected = True
    actual = three_consecutive_odds([3, 5, 7, 2, 4, 6])
    assert actual == expected

def test_no_consecutive_odds():
    expected = False
    actual = three_consecutive_odds([2, 4, 6, 8, 10])
    assert actual == expected

def test_all_odd_numbers():
    expected = True
    actual = three_consecutive_odds([1, 3, 5, 7, 9, 11, 13])
    assert actual == expected

def test_all_even_numbers():
    expected = False
    actual = three_consecutive_odds([2, 4, 6, 8, 10, 12])
    assert actual == expected

def test_single_odd_number():
    expected = None
    actual = three_consecutive_odds([3])
    assert actual == expected

def test_single_even_number():
    expected = None
    actual = three_consecutive_odds([2])
    assert actual == expected

def test_odd_even_odd_numbers():
    expected = False
    actual = three_consecutive_odds([3, 4, 5, 6, 7])
    assert actual == expected

def test_even_odd_even_numbers():
    expected = False
    actual = three_consecutive_odds([2, 3, 4, 5, 6])
    assert actual == expected

def test_odd_even_odd_even_numbers():
    expected = False
    actual = three_consecutive_odds([3, 4, 5, 6, 7, 8])
    assert actual == expected

