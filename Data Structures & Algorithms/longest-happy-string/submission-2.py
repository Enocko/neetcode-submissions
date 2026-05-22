class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = {'a': a, 'b': b, 'c': c}
        maxHeap = [[-y, x] for x, y in h.items() if y != 0]
        heapq.heapify(maxHeap)

        res = ''
        while maxHeap:
            cnt, val = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == val:
                if not maxHeap:
                    break
                cnt2, val2 = heapq.heappop(maxHeap)
                res += val2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(maxHeap, [cnt2, val2])
            else:
                res += val
                cnt += 1
            
            if cnt:
                heapq.heappush(maxHeap, [cnt, val])
        
        return res