# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:        
        res = []
        q = deque()
        q.append(root) if root else None
        
        while(q):
            current = []
            for _ in range(len(q)):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                     q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max(current))
        return res