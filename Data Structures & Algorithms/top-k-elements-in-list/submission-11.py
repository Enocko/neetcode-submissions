class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        maxHeap = [[-c, v] for v, c in h.items()]
        heapq.heapify(maxHeap)

        res = []
        while k > 0:
            c, v = heapq.heappop(maxHeap)
            res.append(v)
            k -= 1
    
        return res