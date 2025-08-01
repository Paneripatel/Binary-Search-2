'''
Problem 2: (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1: Input: [3,4,5,1,2] Output: 1

Example 2: Input: [4,5,6,7,0,1,2] Output: 0
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1    
        while low <= high:
            mid = (low+high) // 2
            if nums[low] <= nums[high]:
                return nums[low]

            if (mid==low or nums[mid] < nums[mid-1]) and (mid==high or nums[mid] < nums[mid+1]):
                return nums[mid]

            if nums[low] <= nums[mid]:
                low = mid+1

            else:
                high = mid-1            