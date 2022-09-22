class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l = s.split(" ")
        for i, word in enumerate(l):
            res += word[::-1]
            if i != len(l)-1 :
                res += " "
        return res