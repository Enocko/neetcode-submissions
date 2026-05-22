class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        k = intervals[0]

        cnt = 0
        for start, end in intervals[1:]:
            if k[1] > start:
                k[1] = min(k[1], end)
                cnt += 1
            else:
                k = [start, end]
                
        
        return cnt
