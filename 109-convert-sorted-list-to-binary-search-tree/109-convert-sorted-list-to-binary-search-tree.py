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
            if l != []:
                mid =len(l)//2
                node = TreeNode(l[mid])
                node.left = root(l[:mid])
                node.right = root(l[mid+1:])
                return node
            else:
                return None
            
        
        if head is None:
            return None
        
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        return root(l)