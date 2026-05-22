class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        h = defaultdict(list)
        for n1, n2 in edges:
            h[n1].append(n2)
            h[n2].append(n1)
        
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in h[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)

