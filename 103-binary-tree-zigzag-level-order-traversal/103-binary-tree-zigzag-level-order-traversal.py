# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque([root])
        i = 1
        while queue:
            current = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            if i%2==0:
                result.append(current[::-1])
            else:
                result.append(current)
            i+=1
        return result