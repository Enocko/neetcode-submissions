class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def dfs(n):
            if n == 1:
                return True
            if n in visited:
                return False
            
            visited.add(n)
            res = 0
            for a in str(n):
                res += int(a) ** 2

            return dfs(res)
        
        return dfs(n)