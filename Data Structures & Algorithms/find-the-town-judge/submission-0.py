class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for x, y in trust:
            outgoing[x] += 1
            incoming[y] += 1
        
        for i in range(1, n+1):
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i
        
        return -1