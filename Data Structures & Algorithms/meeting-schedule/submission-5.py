"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(len(intervals)-1):
            w1 = intervals[i]
            w2 = intervals[i+1]
            if w1.end > w2.start:
                return False
        
        return True