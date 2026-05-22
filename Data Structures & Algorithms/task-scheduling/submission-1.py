class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]

        q = deque()
        t = 0
        while q or maxHeap:
            t += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return t
