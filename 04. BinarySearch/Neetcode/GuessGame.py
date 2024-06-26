"""
https://leetcode.com/problems/guess-number-higher-or-lower/

"""


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            m = (l+r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
            else:
                r = m - 1
            