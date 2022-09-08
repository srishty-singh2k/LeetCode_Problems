# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root):
            if not root: return
            if root.val > val:
                if root.left: insert(root.left)
                else: root.left = TreeNode(val)
            if root.val <= val:
                if root.right: insert(root.right)
                else: root.right = TreeNode(val)
                 
        if not root: return TreeNode(val)
        insert(root)
        return root