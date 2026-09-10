class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(nums):
            r1, r2 = 0, 0
            
            for n in nums:
                tmp = max(n + r1, r2)
                r1 = r2 
                r2 = tmp
            
            return r2
        
        return max(dfs(nums[1:]), dfs(nums[:-1]))

            
