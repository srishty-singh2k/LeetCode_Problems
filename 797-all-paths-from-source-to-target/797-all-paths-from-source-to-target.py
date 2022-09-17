class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(i, path):
            path.append(i)
            if i == n-1:
                paths.append(path)
                return
            for nei in graph[i]:
                dfs(nei, path[:])
            
            
        n = len(graph)
        paths = []
        dfs(0, [])
        return paths