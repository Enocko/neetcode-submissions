class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            k = res[-1]
            if k[1] >= start:
                k[1] = max(k[1], end)
            else:
                res.append([start, end])

        return res
