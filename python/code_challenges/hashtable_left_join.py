from data_structures.hashtable import Hashtable


def find_distinct_elements(nums1, nums2):
    dictionary1 = {}
    dictionary2 = {}

    for num in nums1:
        dictionary1[num] = True

    for num in nums2:
        dictionary2[num] = True

    distinct_nums1 = [num for num in nums1 if num not in dictionary2]
    distinct_nums2 = [num for num in nums2 if num not in dictionary1]

    return [distinct_nums1, distinct_nums2]
