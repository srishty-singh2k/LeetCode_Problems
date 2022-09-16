# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def path(root, p, sum_):
            if not root: return
            p.append(root.val)
            sum_ += root.val
            if not root.left and not root.right:
                if sum_ == targetSum:
                    paths.append(p)
                return
            path(root.left, p[:], sum_)
            path(root.right, p[:], sum_)
                
        paths = []
        path(root, [], 0)
        return paths