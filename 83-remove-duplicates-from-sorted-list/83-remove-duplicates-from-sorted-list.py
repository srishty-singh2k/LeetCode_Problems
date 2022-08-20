# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        s = set()
        while(temp):
            if temp.val in s:
                prev.next = prev.next.next
                temp = temp.next
            else:
                s.add(temp.val)
                prev = temp
                temp = temp.next
        return head