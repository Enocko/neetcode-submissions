class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        maxHeap = [[-c, t] for t, c in h.items()]
        heapq.heapify(maxHeap)

        res = []
        while k > 0:
            c, t = heapq.heappop(maxHeap)
            res.append(t)
            k -= 1
    
        return res
        
