class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1 ,"V":5 ,"X":10 ,"L":50 ,"C":100 ,"D":500, "M":1000}
        sum=0
        i=0
        while(i<len((s))):
            if i==len(s)-1:
                sum+=roman[s[i]]
                i+=1
            elif roman[s[i]]>=roman[s[i+1]]:
                print("+",roman[s[i]])
                sum+=roman[s[i]]
                i+=1
            else:
                print("+",(roman[s[i+1]]-roman[s[i]]))
                sum+=(roman[s[i+1]]-roman[s[i]])
                i+=2
                
        return sum