"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = collections.deque()
        
        q.append(root) if root else None
        
        while(q):
            current = []
            for _ in range(len(q)):
                node = q.popleft()
                current.append(node.val)
                for child in node.children:
                    q.append(child)
                
            if current: res.append(current)
        return res