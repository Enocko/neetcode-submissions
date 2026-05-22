class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            k = bin(i).count('1')
            res.append(k)
        
        return res