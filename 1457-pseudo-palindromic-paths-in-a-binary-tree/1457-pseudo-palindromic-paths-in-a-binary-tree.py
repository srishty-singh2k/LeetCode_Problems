# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def path(root, s):
            if not root: return 0
            if root.val in s:
                s.remove(root.val)
            else:
                s.append(root.val)
            
            if not root.left and not root.right:
                if len(s) <= 1: return 1
            
            return path(root.left, s[:]) + path(root.right, s[:])
            
        return path(root, [])
        