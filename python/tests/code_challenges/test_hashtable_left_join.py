import pytest
from code_challenges.hashtable_left_join import find_distinct_elements

def test_exists():
    assert find_distinct_elements


def test_smallest_interesting_example():
    nums1 = [1,2,3]
    nums2 = [2,4,6]

    output = find_distinct_elements(nums1,nums2)
    expected_output = [[1,3], [4,6]]
    assert output == expected_output

def test_null_example():
    nums1 = []
    nums2 = [1,2,3]

    output = find_distinct_elements(nums1,nums2)
    expected_output = [[], [1,2,3]]
    assert output == expected_output

def test_negative_example():
    nums1 = [-1,2,3]
    nums2 = [1,2,3]

    output = find_distinct_elements(nums1,nums2)
    expected_output = [[-1], [1]]
    assert output == expected_output

def test_my_own_example():
    nums1 = [6,7,8]
    nums2 = [-6,-7,-8]

    output = find_distinct_elements(nums1,nums2)
    expected_output = [[6,7,8], [-6,-7,-8]]
    assert output == expected_output

def test_nulls():
    nums1 = []
    nums2 = []

    output = find_distinct_elements(nums1,nums2)
    expected_output = [[], []]
    assert output == expected_output

def test_repeats():
    nums1 = [1,2,3]
    nums2 = [1,2,3]

    output = find_distinct_elements(nums1,nums2)
    expected_output = [[], []]
    assert output == expected_output

def test_reversed():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    output = find_distinct_elements(nums1,nums2)
    expected_output = [[], []]
    assert output == expected_output

def test_over_sized():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    output = find_distinct_elements(nums1, nums2)
    expected_output = [[], [6, 7, 8, 9, 10]]
    assert output == expected_output

def test_uniques():
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7, 8]
    output = find_distinct_elements(nums1, nums2)
    expected_output = [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert output == expected_output

