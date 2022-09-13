class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [0 for i in range(len(text2)+1)]
        print(row)
        for i in range(1, len(text1)+1):
            dp = [0 for i in range(len(text2)+1)]
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1 + row[j-1]
                else:
                    dp[j] = max(row[j], dp[j-1])
            row = dp
        return row[-1]