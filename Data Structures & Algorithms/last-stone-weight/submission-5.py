class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-c for c in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a < b:
                heapq.heappush(stones, a - b)
        
        stones.append(0)
        return abs(stones[0])
            
    

"""
[-6, -4, -3, -2, -2]

"""