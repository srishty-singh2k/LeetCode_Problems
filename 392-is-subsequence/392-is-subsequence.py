class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1 = i2 = 0
        s1 = t
        s2 = s
        while(i1 < len(s1)):
            if i2 < len(s2) and s1[i1] == s2[i2]:
                i2 += 1
            i1 += 1
        if i2 < len(s2):
            return False
        return True