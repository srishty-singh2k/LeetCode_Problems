# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inOrder = self.inorder(root,[])
        for i in range(1,len(inOrder)):
            if inOrder[i]<=inOrder[i-1]:
                return False
        return True
    
    
    
    def inorder(self,root,res):
        if root!=None:
            self.inorder(root.left,res)
            res.append(root.val)
            self.inorder(root.right,res)
        return res
        