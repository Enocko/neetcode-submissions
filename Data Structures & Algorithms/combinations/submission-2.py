class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        stack = []

        def dfs(i):
            if len(stack) == k:
                res.append(stack[:])
                return 
            
            if i >= len(nums):
                return 
            
            stack.append(nums[i])
            dfs(i+1)

            stack.pop()
            dfs(i+1)
        
        dfs(0)
        return res

        