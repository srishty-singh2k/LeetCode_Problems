# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        elif list1==None:
            return list2
        elif list2==None:
            return list1
        res = None
        head = None
        while(list1!=None and list2!=None):  
            print(list1.val,list2.val)
            if list1.val<=list2.val:
                temp = ListNode()
                temp.val=list1.val
                if head==None:
                    res=temp
                    head=temp
                else: 
                    head.next=temp
                    head=temp
                list1=list1.next
                print("From1",res,head)
            elif list1.val>list2.val:
                temp = ListNode()
                temp.val=list2.val
                if head==None:
                    res=temp
                    head=temp
                else: 
                    head.next=temp
                    head=temp
                list2=list2.next
                print("From2",res,head)

        if(list1==None and list2==None):
            return res
        if(list1!=None):
            while(list1!=None):
                temp=ListNode()
                temp.val=list1.val
                head.next = temp
                head=temp
                list1=list1.next
            return res
        if(list2!=None):
            while(list2!=None):
                temp=ListNode()
                temp.val=list2.val
                head.next = temp
                head=temp
                list2=list2.next
            return res

            
            
            
            
            
            
            