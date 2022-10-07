# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        inorderl = []
        
        def inorder(root):
            if root:
                inorder(root.left)
                inorderl.append(root.val)
                inorder(root.right)
        
        inorder(root)
        
        dic = {}
        
        
        for i in inorderl:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
                
        maxim = max(dic.values())
        
        res = []
        for i in dic:
            if dic[i]==maxim:
                res.append(i)
                
        return res        