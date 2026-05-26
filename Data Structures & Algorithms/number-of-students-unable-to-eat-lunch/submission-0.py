class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        h = Counter(students)
        res = len(students)

        for n in sandwiches:
            if h[n] > 0:
                h[n] -= 1
                res -= 1
            else:
                break
        
        return res
        
