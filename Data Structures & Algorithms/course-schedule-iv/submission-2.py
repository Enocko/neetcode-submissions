class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        h = defaultdict(list)
        for pre, crs in prerequisites:
            h[crs].append(pre)
        
        def dfs(crs):
            if crs not in dict:
                for pre in h[crs]:
                    dict[crs] |= dfs(pre)
                dict[crs].add(crs)

            return dict[crs]

        dict = defaultdict(set)
        for i in range(numCourses):
            dfs(i)

        res = []
        for u,v in queries:
            res.append(u in dict[v])
    
        return res