# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def path(root, s):
            if not root: return 0
            if not root.left and not root.right:
                nonlocal sum_ 
                sum_ += int(s + str(root.val))
            path(root.left, s + str(root.val))
            path(root.right, s + str(root.val))
                
        sum_ = 0
        path(root, "") if root else None
        return sum_