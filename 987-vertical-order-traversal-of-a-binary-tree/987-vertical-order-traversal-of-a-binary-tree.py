# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        g = collections.defaultdict(list)
        q = deque()
        q.append([root, 0])
        
        while(q):
            
            d = collections.defaultdict(list)
            for _ in range(len(q)):
                
                node, col = q.popleft()
                d[col].append(node.val)
                if node.left:
                    q.append([node.left, col-1])
                if node.right:
                    q.append([node.right, col+1])
                
            for c in d: g[c].extend(sorted(d[c]))
        
        return [g[c] for c in sorted(g)]
        