# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def su(root):
            if not root:
                return 0
            left = su(root.left)
            right=su(root.right)
            
            return left+right+root.val
        
        
        total = su(root)
        self.mini = float('inf')
        self.maxi = float('-inf')
            
        def helper(root):
            if not root:
                return 0
                
            left = helper(root.left)
            right = helper(root.right)
                
            s = total-(left+right+root.val)
            a = abs((left+right+root.val)-s)
            if a<self.mini and (left+right+root.val)>self.maxi:
                self.mini = a
                self.maxi = left+right+root.val
            return (left+right+root.val)
            
        helper(root)
        return (self.maxi*(total-self.maxi))%((10**9)+7)
        