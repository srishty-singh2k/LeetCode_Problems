# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        rev = ListNode(0)
        tail = rev
        while(True):
            kth = head
            c = 1
            while(kth and c<k):
                kth = kth.next
                c += 1
            if not kth:
                tail.next = head
                break
            gNext = kth.next
            gEnd = head
            
            while(head != gNext):
                curr = head
                head = head.next
                curr.next = tail.next
                tail.next = curr
            
            tail = gEnd
            
        return rev.next
            
    
    
            
            
        