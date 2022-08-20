# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        d = {}
        while(temp):
            if temp.val not in d:
                d[temp.val] = 1
            else:
                d[temp.val] += 1
            temp = temp.next
        
        temp = head
        prev = None
        while(temp):
            if d[temp.val] == 1:
                prev = temp
                temp = temp.next
            else:
                temp = temp.next
                if (prev is not None):
                    prev.next = temp
                else:
                    head = head.next
        return head