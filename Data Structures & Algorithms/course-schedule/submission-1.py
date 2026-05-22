class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h = defaultdict(list)
        for crs, pre in prerequisites:
            h[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if h[crs] == []:
                return True
            
            visited.add(crs)
            for pre in h[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            h[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True