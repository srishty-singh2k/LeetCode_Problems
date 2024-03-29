"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        d = {node: Node(node.val)}
        q = []
        q.append(node)
        vis = set()
        
        while(q):
            curr = q.pop()
            vis.add(curr)
                
            for n in curr.neighbors:
                if n not in vis and n not in q:
                    q.append(n)
                if n not in d:
                    d[n] = Node(n.val)
                d[curr].neighbors.append(d[n])
                
        return d[node]