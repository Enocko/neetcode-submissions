class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = defaultdict(int)
        
        for x, y in trust:
            res[x] -= 1
            res[y] += 1
        
        for k in res.keys():
            if res[k] == n - 1:
                return k
        
        return -1
        
