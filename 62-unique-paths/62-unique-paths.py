class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(1,m):
            newRow = [1]*n
            for j in range(1,n):
                newRow[j] = row[j] + newRow[j-1]
            row = newRow
        return row[-1]
