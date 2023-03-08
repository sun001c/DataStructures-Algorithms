"""
https://leetcode.com/problems/decode-ways/

Approach: this is another case for bottom to top dynamic programming
i haven't understood the logic well why do we need i+2

Approach: O(n)
Sc: O(n)

"""

def decodeWays(s):
    dp = {}
    dp[len(s)] = 1

    for i in range(len(s)-1 , -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
        
        if i+1 < len(s) and (
            s[i] == "1" or (s[i] == "2" and s[i+1] in ('0123456'))):
            dp[i] += dp[i+2]
        
    return dp[0]