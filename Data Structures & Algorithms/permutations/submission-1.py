class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def dfs():
            if len(stack) == len(nums):
                res.append(stack[:])
                return 
            
            for n in nums:
                if n not in stack:
                    stack.append(n)
                    dfs()
                    stack.pop()
            
        dfs()
        return res
