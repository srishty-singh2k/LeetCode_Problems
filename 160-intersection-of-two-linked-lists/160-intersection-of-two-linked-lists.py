# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 1
        lenB = 1
        tempA = headA
        tempB = headB
        while (tempA.next):
            lenA+=1
            tempA = tempA.next
        while (tempB.next):
            lenB+=1
            tempB = tempB.next
        
        if (tempA == tempB):
            i = 0
            if (lenA>lenB):
                while(i<(lenA-lenB)):
                    i+=1
                    headA = headA.next
            elif (lenA<lenB):
                while(i<(lenB-lenA)):
                    i+=1
                    headB = headB.next
            while(headA):
                if(headA == headB):
                    return headA
                headA = headA.next
                headB = headB.next
            
        return None