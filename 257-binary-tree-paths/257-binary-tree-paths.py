# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def path(root, s):
            if not root: return
            if not root.left and not root.right:
                res.append(s+str(root.val))
            
            path(root.left, s+str(root.val)+"->")
            path(root.right, s+str(root.val)+"->")
            
        res = []
        path(root, "") if root else None
        return res