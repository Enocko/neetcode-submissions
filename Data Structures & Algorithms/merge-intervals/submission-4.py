class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        k = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if k[1] >= start:
                k = [min(k[0], start), max(k[1], end)]
            else:
                res.append(k)
                k = [start, end]
        
        res.append(k)
        return res
