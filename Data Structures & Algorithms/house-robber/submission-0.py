class Solution:
    def rob(self, nums: List[int]) -> int:
        # r1, r2 = 0, 0

        # for n in nums:
        #     tmp = max(r1+n, r2)
        #     r1 = r2
        #     r2 = tmp 
        
        # return r2

        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[n-1]
        