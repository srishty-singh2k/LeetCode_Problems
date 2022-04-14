class Solution:
    def isValid(self, s: str) -> bool:
        brackets=["()","[]","{}"]
        flag=0
        for each in brackets:    
            while(each in s):
                s= s.replace(each, "")
                flag=1
        if s=="":
            return True
        if s!="" and flag==0:
            print(s)
            return False
        return self.isValid(s)