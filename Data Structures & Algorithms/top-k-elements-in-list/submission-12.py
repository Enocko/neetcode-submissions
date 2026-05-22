class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        maxHeap = [[-c, key] for key, c in h.items()]
        heapq.heapify(maxHeap)

        res = []
        while k > 0:
            cnt, val = heapq.heappop(maxHeap)
            res.append(val)
            k -= 1
        
        return res

        # {
        #     1: 1,
        #     2: 2,
        #     3: 3
        # }

        # [[-1, 1], [-2, 2], [-3, 3]]
        # [[-3, 3], [-2, 2], [-1, 1]]
        # [-3, 3]
        