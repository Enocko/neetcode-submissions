class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        stack = []

        def dfs(i):
            if len(stack) == k and stack not in res:
                res.append(stack[:])

            if i >= n:
                return 

            stack.append(nums[i])
            dfs(i+1)

            stack.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)   

        dfs(0)    
        return res