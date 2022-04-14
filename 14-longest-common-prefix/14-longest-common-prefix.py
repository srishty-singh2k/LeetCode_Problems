class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1 :
            return strs[0]
        if "" in strs:
            return ""
        for i in range(len(min(strs, key=len))):
            for each in strs[1:]:
                if strs[0][i]!=each[i]:
                    return strs[0][:i]
        
        
        return strs[0][:i+1]