# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        fast = slow = head
        rev = None
        temp = None
        while(fast and fast.next):
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = rev
            rev = temp
        if fast and fast.next is None:
            slow = slow.next
        while(slow):
            if slow.val == rev.val:
                slow = slow.next
                rev = rev.next
            else:
                return False
        return True