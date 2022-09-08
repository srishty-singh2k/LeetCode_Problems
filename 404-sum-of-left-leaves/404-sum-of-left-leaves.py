# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def leftLeaf(root, left):
            if not root: return 0
            if not root.left and not root.right:
                return root.val if left else 0
            return leftLeaf(root.left, True) + leftLeaf(root.right, False)
        
        return leftLeaf(root, False)
        
        