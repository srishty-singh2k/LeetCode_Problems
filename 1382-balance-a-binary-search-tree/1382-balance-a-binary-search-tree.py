# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        l = []
        inorder(root)
        
        def insert(l):
            if len(l)==0:
                return None
            if len(l)==1:
                return TreeNode(l[0])
            left = l[:len(l)//2]
            right = l[len(l)//2+1:]
            node = TreeNode(l[len(l)//2])
            node.left = insert(left)
            node.right = insert(right)
            return node
            
        root = insert(l)
        return root