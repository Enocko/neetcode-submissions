class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        pars = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(a):
            pa = pars[a]

            while pa != pars[pa]:
                pa = pars[pa]
            
            return pa
        
        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            
            if rank[pa] > rank[pb]:
                rank[pa] += rank[pb]
                pars[pb] = pars[pa]
            else:
                rank[pb] += rank[pa]
                pars[pa] = pars[pb]
            
            return True
        
        res = []

        for u,v in edges:
            if not union(u,v):
                res.append([u,v])
       
        return res[-1]
        