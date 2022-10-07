# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.val = 0
        
        def helper(root):
            
            if root:
                if not root.left and not root.right:
                    self.val+=root.val
                    root.val = self.val
                    return
                helper(root.right)
                self.val+=root.val
                root.val = self.val
                helper(root.left)
            
        helper(root)
        return root
            
                
            
        