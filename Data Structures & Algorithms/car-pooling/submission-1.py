class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1000
        for passenger, start, end in trips:
            timeline[start] += passenger
            timeline[end] -= passenger
        
        res = 0
        for n in timeline:
            res += n
            if res > capacity:
                return False
        
        return True
