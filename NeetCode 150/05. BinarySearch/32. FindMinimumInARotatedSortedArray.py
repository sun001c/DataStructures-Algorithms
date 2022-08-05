"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Approach: binary search as they are sorted. 
return the left element as we need the minimum 

TC: O(logn) as it is a binary search
SC: O(1) no additional space is required
"""


def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:  # compute the value after the while loop
        mid = (left + right) // 2
        if nums[mid] < nums[right]:  # compare the value with the right to find if it is rotated
            right = mid
        elif nums[mid] > nums[right]:
            left = mid+1
    return nums[left]


print(findMin([3, 4, 5, 1, 2]))