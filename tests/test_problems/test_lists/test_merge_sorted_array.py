
"""
Test Suite for the maximum-subarray
"""
from problems.list.merge_sorted_array import Solution


class TestMergeSortedArray:
    """
    Test Class
    """
    def test_one(self):
        nums1 = [1,2,3,0,0,0]
        old_id = id(nums1)
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]
        Solution().merge(nums1, m, nums2, n)
        new_id = id(nums1)
        # checking the nums1 list identity before and after merge.
        assert old_id == new_id 
        assert nums1 == expected


    def test_two(self):
        nums1 = [1]
        old_id = id(nums1)
        m = 1
        nums2 = []
        n = 0
        expected = [1]
        Solution().merge(nums1, m, nums2, n)
        new_id = id(nums1)
        assert old_id == new_id
        assert nums1 == expected


    def test_three(self):
        nums1 = [0]
        old_id = id(nums1)
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        Solution().merge(nums1, m, nums2, n)
        new_id = id(nums1)
        assert old_id == new_id
        assert nums1 == expected
