# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root,[])
    
    
    def inorder(self,root,res):
        if root!=None:
            res.append(root.val)
            self.inorder(root.left,res)
            self.inorder(root.right,res)
        return res
          