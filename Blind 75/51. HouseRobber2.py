"""
https://leetcode.com/problems/house-robber-ii/

Approach: this is similar to house robber but circular. 
so we can either take 0 to n-2 or 1 to n-1 to avoid adjacency. nice cool trick

Tc: O(n)
Sc: O(n)

"""

class Solution():
    def houseRobber2(self, nums):
        return max(
            nums[0], 
            self.houseRobber1(nums[0:len(nums)-1]), 
            self.houseRobber1(nums[1:])
        )
    
    def houseRobber1(self, nums):
        prev2, prev = 0, 0
        ans = 0
        for num in nums:
            curr = max(prev2 + curr, prev)
            prev2 = prev
            prev = curr
            ans = max(ans, curr)
        return ans



