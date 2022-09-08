class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(0, m):
            for j in range(0, n):
                if i==0 and j==0: continue
                else:
                    up = grid[i-1][j] if i-1>=0 else float('inf')
                    left = grid[i][j-1] if j-1>=0 else float('inf')
                    grid[i][j] += min(up, left)
        return grid[m-1][n-1]