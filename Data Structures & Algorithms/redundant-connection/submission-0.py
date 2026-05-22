class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
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
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]