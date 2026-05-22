class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1] * n

        def find(a):
            res = par[a]
            while res != par[res]:
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False     
                
            elif rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]
            return True

        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        
        return res
