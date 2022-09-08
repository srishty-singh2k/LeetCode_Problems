# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def leftLeaf(root, left):
            if not root: return
            if left and not root.left and not root.right:
                nonlocal sum_
                sum_ += root.val
            leftLeaf(root.left, True)
            leftLeaf(root.right, False)
        sum_ = 0
        leftLeaf(root.left, True)
        leftLeaf(root.right, False)
        return sum_
        