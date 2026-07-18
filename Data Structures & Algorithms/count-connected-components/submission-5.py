class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1] * n

        def find(a):
            while a != par[a]:
                a = par[a]
            
            return a 
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return False 
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True 
        
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        
        return res