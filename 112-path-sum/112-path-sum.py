# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(root, targetSum, total):
            if not root:
                return False
            if not root.left and not root.right :
                return root.val+total == targetSum
            
            return pathSum(root.left, targetSum, root.val+total) or pathSum(root.right, targetSum, root.val+total)
                
        if not root:
            return False
        return pathSum(root, targetSum, 0)