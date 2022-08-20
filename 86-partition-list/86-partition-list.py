# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        temp = head
        prev = None
        right = None
        while(temp):
            if temp.val >= x:
                node = temp
                temp = temp.next
                if(prev is None):
                    head = head.next
                else:
                    prev.next = temp
                    
                if (right):
                    rtemp = right
                    while(rtemp.next):
                        rtemp = rtemp.next
                    rtemp.next = node
                else:
                    right = node
                node.next = None
            else:
                prev = temp
                temp = temp.next
        if prev:
            prev.next = right
            return head
        else:
            return right
