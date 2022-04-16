# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            head=None
            return head
        ptr=head
        val=[]
        while(ptr!=None):
            val.append(ptr.val)
            ptr=ptr.next
        
        index=len(val)-n
        
        if index==0:
            head=head.next
            return head
        
        index-=1
        counter=0
        ptr=head
        while(counter<index):
            ptr=ptr.next
            counter+=1
        ptr.next=(ptr.next).next
        return head
