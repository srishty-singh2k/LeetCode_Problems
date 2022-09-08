# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.previous = self.minimum = float('inf')

        def inorder(node):
            if node:
                inorder(node.left)
                self.minimum = min(self.minimum, abs(node.val-self.previous))
                self.previous = node.val
                inorder(node.right)

        inorder(root)
        return self.minimum