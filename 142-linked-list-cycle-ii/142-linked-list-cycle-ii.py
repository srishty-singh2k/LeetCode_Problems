# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None: # If we ever find one node point to None means it can form a cycle 
            return None
        
        first = head.next
        second = head.next.next

        
        while first != second: # If we ever find one node point to None means it can form a cycle 
            if second is not None:
                first = first.next
                second = second.next
                second = second.next if second is not None else None
            else:
                return None
            
        first = head
            
        while first != second:
            first = first.next
            second = second.next
        return first