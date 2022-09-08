# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        l = []
        inorder(root)
        return min(b - a for a, b in zip(l, l[1:]))