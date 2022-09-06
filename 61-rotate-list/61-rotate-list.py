# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head: return head
        fast = slow = head
        i = 1
        while(i<=k and fast):
            fast = fast.next
            i+=1
        if fast:
            while(fast.next):
                fast = fast.next
                slow = slow.next
            temp = slow.next
            slow.next = None
            fast.next = head
            head = temp
            return head
        if k % (i-1) == 0:
            return head
        return self.rotateRight(head, k%(i-1))
            
            