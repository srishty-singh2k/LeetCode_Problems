# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        fast = head
        prev = None
        while(True):
       
            if (fast.next == None ):
                head = head.next
                break
            elif fast.next.next == None:
                temp = head
                head = head.next
                temp.next = prev
                prev = temp
                break
            else:
                fast = fast.next.next
                     
                temp = head
                head = head.next
                temp.next = prev
                prev = temp
            
        while(head):
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True