# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head: return head
        current = head
        len_ = 1
        while(current.next):
            current = current.next
            len_ += 1
        if k % len_ == 0:
            return head
        current.next = head
        k = len_ - (k%len_)
        while(k):
            current = current.next
            k-=1
        head = current.next
        current.next = None
        return head
            