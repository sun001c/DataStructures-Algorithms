"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

APPROACH: 
Have a helper function where you pass the nodea and the maxValue so far. 
if the node.val is greater than maxValue , we increase the output by 1
repeat for left and right nodes. 

O(n) traverse every node once
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxi):
            res = 0
            if not root:
                return 0
            if root.val >= maxi:
                res += 1
                maxi = root.val
            res += dfs(root.left, maxi)
            res += dfs(root.right, maxi)
            
            return res
        
        return dfs(root, root.val)
    

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        maxi = root.val
        q.append((root, root.val))
        while q:
            for i in range(len(q)):
                node, maxi = q.popleft()
                if node:
                    if node.val >= maxi:
                        res += 1
                        maxi = node.val
                    if node.left:
                        q.append((node.left, maxi))
                    if node.right:
                        q.append((node.right, maxi))
        
        return res
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append((root, root.val))
        res = 1
        while q:
            for i in range(len(q)):
                node, curr = q.popleft()
                if node:
                    if node.left:
                        if node.left.val >= curr:
                            res += 1
                            q.append((node.left, node.left.val))
                        else:
                            q.append((node.left, curr))
                    
                    if node.right:
                        if node.right.val >= curr:
                            res += 1
                            q.append((node.right, node.right.val))
                        else:
                            q.append((node.right, curr))
        return res              
                
        