class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        minHeap = [ [c,p] for c, p in zip(capital, profits)]
        heapq.heapify(minHeap)

        for i in range(k):

            while minHeap and minHeap[0][0] <= w:
                c, p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -1 * p)
            
            if not maxHeap:
                break
            w += -1 * heapq.heappop(maxHeap)
        
        return w
