class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for i in range(len(text2)+1)]
        for i in range(1, len(text1)+1):
            curr = [0 for i in range(len(text2)+1)]
            for j in range(len(text2)+1):
                if j == 0:
                    curr[j] = 0
                elif text1[i-1] == text2[j-1]:
                    curr[j] = 1 + dp[j-1]
                else:
                    curr[j] = max(curr[j-1], dp[j])
            dp = curr
        return dp[-1]