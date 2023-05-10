"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = collections.deque()
        q.append((root, 1))
        res = float('inf')
        
        while q:
            for i in range(len(q)):
                node, ind = q.popleft()
                if node:
                    if not node.left and not node.right:
                        res = min(res, ind)
                        
                    q.append((node.left, ind+1))
                    q.append((node.right, ind+1))
        return res
