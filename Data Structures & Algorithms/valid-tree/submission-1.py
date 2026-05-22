class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        h = defaultdict(list)
        for crs, pre in edges:
            h[crs].append(pre)
            h[pre].append(crs)
        
        visited = set()
        def dfs(crs, previous):
            if crs in visited:
                return False
            visited.add(crs)
            for pre in h[crs]:
                if pre == previous:
                    continue
                if not dfs(pre, crs):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)