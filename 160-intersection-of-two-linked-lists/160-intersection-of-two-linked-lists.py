# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        tempA = headA
        while(tempA):
            d[tempA] = True
            tempA = tempA.next
        
        tempB = headB
        while(tempB):
            if tempB in d:
                return tempB
            tempB = tempB.next
        return None