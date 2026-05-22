class Solution:
    def reorganizeString(self, s: str) -> str:
        h = Counter(s)
        maxHeap = [[-c, k] for k, c in h.items()]

        prev = None
        res = ''
        while maxHeap or prev:
            if not maxHeap and prev:
                return ''
            cnt, val = heapq.heappop(maxHeap)
            res += val
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt:
                prev = [cnt, val]
        
        return res