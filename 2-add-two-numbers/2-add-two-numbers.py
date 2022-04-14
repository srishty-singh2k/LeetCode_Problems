# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #print((((l1.next).next).next))
        res=None
        head=None
        c=0
        
        while(l1!=None and l2!=None):
            s=l1.val+l2.val+c
            c=0
            if s>=10:
                c=s//10
                s=s%10
            temp=ListNode()
            temp.val=s
            if res==None:
                res = temp
                head = temp
            else:
                head.next = temp
                head=temp
            l1=l1.next
            l2=l2.next
            #print("End ",s, c, temp.val, l1, l2)
        
        if l1==None and l2==None and c==0:
            return res
        if l1==None and l2==None and c!=0:
            temp=ListNode()
            temp.val=c
            head.next = temp
            return res
        if l1!=None:
            while(l1!=None or c!=0):
                if (l1==None):
                    s=c
                else:
                    s=l1.val+c
                    l1=l1.next
                c=0
                if s>=10:
                    c=s//10
                    s=s%10
                temp=ListNode()
                temp.val=s
                head.next = temp
                head=temp
            
            return res
        if l2!=None:
            while(l2!=None or c!=0):
                if (l2==None):
                    s=c
                else:
                    s=l2.val+c
                    l2=l2.next
                c=0
                if s>=10:
                    c=s//10
                    s=s%10
                temp=ListNode()
                temp.val=s
                head.next = temp
                head=temp
            
            return res
                
            
