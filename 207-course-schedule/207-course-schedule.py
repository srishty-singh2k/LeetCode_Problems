class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = { i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            pre[c].append(p)
        vis = set()
        
        def dfs(crs):
            if crs in vis:
                return False
            if pre[crs] == []:
                return True
            
            vis.add(crs)
            for p in pre[crs]:
                if not dfs(p): return False
            
            vis.remove(crs)
            pre[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        

            