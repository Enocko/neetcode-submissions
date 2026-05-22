class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        pars = list(range(n))

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
        
        total = n

        for a,b in edges:
            if union(a,b):
                total -= 1
        
        return total
        
