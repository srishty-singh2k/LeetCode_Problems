class Solution:
    def isPalindrome(self, each:str) -> bool:
        print("To check: ",each)
        if len(each)%2==0:
            if  ("".join(reversed(each[:len(each)//2]))) == each[len(each)//2:]:
                return True
        else:
            if ("".join(reversed(each[:len(each)//2+1]))) == each[len(each)//2:]:
                return True
        return False

                    
    def longestPalindrome(self, s: str) -> str:
        pali=[]
        even=[]
        for each in s:
            pali.append(each)
        #print(pali)
        for i in range(len(s)-1):
            offset=0
            if s[i] == s[i+1]:
                even.append(i)
                while(i-offset>-1 and i+1+offset<len(s) and s[i-offset]==s[i+offset+1]):
                    if i+offset+2 ==len(s):
                        pali.append(s[i-offset:])
                    else:
                        pali.append(s[i-offset: i+offset+2])
                    offset+=1
            offset=0
            while(i-offset>-1 and i+offset<len(s) and s[i-offset]==s[i+offset]):
                #print("odd", i, offset, s[i-offset]==s[i+offset])
                if i+offset+1 ==len(s):
                    pali.append(s[i-offset:])
                else:
                    pali.append(s[i-offset: i+offset+1])
                offset+=1
                
        #print("pali",pali)
        #print("even",even)
        
        if pali==[]:
            return ""
        return max(pali, key=len)