class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = [0] * 1000

        for x, y, z in trips:
            h[y] += x
            h[z] -= x
        
        res = 0
        for i in range(len(h)):
            res += h[i]
            if res > capacity:
                return False
        
        return True