class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
        
        while(q):
            for _ in range(len(q)):
                i, j = q.popleft()
                if i+1 < m and grid[i+1][j] == 1:
                    q.append([i+1, j])
                    grid[i+1][j] = 2
                if i-1 >= 0 and grid[i-1][j] == 1:
                    q.append([i-1, j])
                    grid[i-1][j] = 2
                if j+1 < n and grid[i][j+1] == 1:
                    q.append([i, j+1])
                    grid[i][j+1] = 2
                if j-1 >= 0 and grid[i][j-1] == 1:
                    q.append([i, j-1])
                    grid[i][j-1] = 2
            if q:
                time += 1
            
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time
        