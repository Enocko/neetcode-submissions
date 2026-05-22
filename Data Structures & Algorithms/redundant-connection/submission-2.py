class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges)+1))
        rank = [1] * (1 + len(edges))

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
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]