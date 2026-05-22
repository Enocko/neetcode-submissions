class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001
        for x,y,z in trips:
            timeline[y] += x
            timeline[z] -= x
        
        res = 0
        for i in range(len(timeline)):
            res += timeline[i]
            if res > capacity:
                return False
        
        return True
