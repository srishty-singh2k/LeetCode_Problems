# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def root(l):
            val = l[len(l)//2]
            node = TreeNode(val)
            if len(l) == 1:
                return node
            elif len(l) == 2:
                node.left = root(l[:len(l)//2])
                return node
            node.left = root(l[:len(l)//2])
            node.right = root(l[len(l)//2+1:])
            return node
        
        if head is None:
            return None
        
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        return root(l)