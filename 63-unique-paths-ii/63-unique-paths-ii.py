class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0
        dp = [[-1]*n]*m
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    dp[i][j] = 1
                    print("a")
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    print("b")
                else:
                    print("d")
                    up = dp[i-1][j] if i-1>=0 else 0
                    left = dp[i][j-1] if j-1>=0 else 0
                    dp[i][j] = up+left
        
        print(dp)                
        return dp[m-1][n-1]
