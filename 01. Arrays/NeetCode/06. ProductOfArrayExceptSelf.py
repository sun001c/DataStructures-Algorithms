"""
https://leetcode.com/problems/product-of-array-except-self/

APPROACH: 
for any number, we want to calculate the prefix product and postfix product. 
iterate through the array from start and then iterate through the array from end.
[1,2,3,4] after first iteration [1,1,2,6] after second iteration [24,12,8,6]

TC: O(n) we are iterating through the loop
SC: O(n) we are creating an array 

FOLLOW-UP: WITHOUT ADDITIONAL SPACE
"""

def product(nums):
    res = []
    p = 1
    for i in range(len(nums)):
        res.append(p)  # we are calculating prefix product here
        p *= nums[i]  # update prefix

    p = 1
    for i in range(len(nums)-1, -1, -1):  # postfix operator here
        res[i] *= p  # multiply prefix and postfix
        p *= nums[i]  # update postfix
    return res
