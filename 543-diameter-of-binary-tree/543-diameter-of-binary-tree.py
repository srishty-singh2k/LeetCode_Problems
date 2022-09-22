# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.height(root)[0]
        

    def height(self, root):
        if not root: return 0, -1
        if not root.left and not root.right: return 0, 0
        ld, l = self.height(root.left)
        rd, r = self.height(root.right)
        dia = max(l+r+2, ld, rd)
        return dia, max(l, r)+1