class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h = defaultdict(int)

        for x, y in trust:
            h[x] -= 1
            h[y] += 1
        
        for k, v in h.items():
            if v == n - 1:
                return k
        
        return -1



"""
h = {
    1: -1,
    2: -1
    3: 3,
    4: -1,

}

"""