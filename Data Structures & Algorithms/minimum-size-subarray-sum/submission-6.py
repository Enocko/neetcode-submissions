class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        cnt = 0
        l = 0

        for r in range(len(nums)):
            cnt += nums[r]
            while cnt >= target:
                res = min(res, r - l + 1)
                cnt -= nums[l]
                l += 1
        
        return 0 if res == float('inf') else res