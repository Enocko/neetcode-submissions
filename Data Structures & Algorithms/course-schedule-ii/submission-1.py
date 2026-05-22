class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        h = defaultdict(list)
        for crs, pre in prerequisites:
            h[crs].append(pre)
        
        output = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in h[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return output

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output