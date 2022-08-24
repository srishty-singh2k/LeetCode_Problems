class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1 = i2 = 0
        while(i1 < len(t)):
            if i2 < len(s) and t[i1] == s[i2]:
                i2 += 1
            i1 += 1
        if i2 < len(s):
            return False
        return True