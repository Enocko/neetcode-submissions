class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                Ind, temp = stack.pop()
                res[Ind] = i - Ind
            
            stack.append([i, t])
        
        return res