# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.calc(root)
        
    def calc(self, root):
        if(root.left != None):
            if(root.val == 2):
                return self.calc(root.left) or self.calc(root.right)
            else:
                return self.calc(root.left) and self.calc(root.right)
        else:
            return True if root.val==1 else False
