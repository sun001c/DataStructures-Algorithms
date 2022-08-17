"""

https://leetcode.com/problems/merge-intervals/

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Approach: First we need to sort them based on the intervals[i][0]. 
Now, add the first interval and iterate through the rest of them and check if the start is less than end of the last interval
then try to find the max of those two intervals. 
else, append the interval to the result. 

TC O(nlogn) as we are sorting here
SC: O(n) we are using a res array.

"""


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        last = res[-1][1]

        for s, e in intervals[1:]:
            if s <= last:  # if they overlap find the max and update the res with max
                last = max(last, e)
                res[-1][1] = last
            else:  # if they don't overlap add the interval and update the last
                res.append([s, e])
                last = e

        return res
