class Solution:
    def reorganizeString(self, s: str) -> str:
        h = Counter(s)
        maxHeap = [[-y, x] for x, y in h.items()]
        heapq.heapify(maxHeap)

        res = ''
        prev = None
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