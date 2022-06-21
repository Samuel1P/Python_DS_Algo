"""
Test Suite for the 
"""
import pytest
import random
from algorithms.Sorting.Quick_Sort_in_place import quick_sort


class TestQuickSort:
    """
    Test Class
    """

    def test_sort_list_one(self):
        test_list = [4,6,1,7,3,2,5]
        last_index = len(test_list) - 1 
        actual = quick_sort(test_list, 0, last_index)
        expected = sorted(test_list)
        assert actual == expected

    def test_sort_list_two(self):
        test_list = random.sample(range(1, 100000), 786)
        last_index = len(test_list) - 1 
        actual = quick_sort(test_list, 0, last_index)
        expected = sorted(test_list)
        assert actual == expected

    def test_sort_list_three(self):
        test_list = random.sample(range(-10000, 100000), 7862)
        last_index = len(test_list) - 1 
        actual = quick_sort(test_list, 0, last_index)
        expected = sorted(test_list)
        assert actual == expected