# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def path(root, cur):
            if not root: return 0
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                return cur
            return path(root.left, cur) + path(root.right, cur)
        return path(root, 0)