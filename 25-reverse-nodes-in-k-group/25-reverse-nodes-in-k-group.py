# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        s1 = []
        s2 = []
        counter = 1
        rev = None
        
        while(head):
            if counter <= k:
                s1.append(head)
                head = head.next
            if counter == k:
                while(s1):
                     s2.append(s1.pop())
                counter = 1
            else:
                counter += 1
        print([n.val for n in s1], [n.val for n in s2])

        while(s1):
            node = s1.pop()
            node.next = rev
            rev = node
        while(s2):
            node = s2.pop()
            node.next = rev
            rev = node
        return rev
            
            
        