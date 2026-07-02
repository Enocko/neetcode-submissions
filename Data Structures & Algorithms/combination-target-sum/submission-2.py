class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def dfs(i):
            if sum(stack) == target:
                res.append(stack[:])
                return 
            
            if i >= len(nums) or sum(stack) > target:
                return 
            
            stack.append(nums[i])
            dfs(i)

            stack.pop()
            dfs(i+1)
        
        dfs(0)
        return res