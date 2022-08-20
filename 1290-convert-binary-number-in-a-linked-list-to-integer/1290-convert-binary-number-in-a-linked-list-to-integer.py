# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        rev = None
        while(head):
            temp = head
            head = head.next
            temp.next = rev
            rev =temp
        
        value = 0
        count = 0
        while(rev):
            if rev.val == 1:
                value += 2**count
            count+=1
            rev = rev.next
        return value