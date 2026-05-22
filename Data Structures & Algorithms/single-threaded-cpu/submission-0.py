class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda t: t[0])

        res, maxHeap = [], []
        i, time = 0, tasks[0][0]
        while maxHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(maxHeap, [tasks[i][1], tasks[i][2]])
                i += 1
        
            if not maxHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(maxHeap)
                res.append(index)
                time += procTime
    
        return res