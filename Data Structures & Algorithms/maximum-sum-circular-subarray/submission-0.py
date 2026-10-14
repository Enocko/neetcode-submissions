class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)

            total += n
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
    
        return max(globMax, total - globMin) if globMax > 0 else globMax



"""
globMax = -2
globMin = -2

curMax, curMin = 0, 0
total = 0

for n in nums:
    curMax = max(0, -2)
    curMin = min(0, -2) # -2

    total += n  # -2
    globalMax = max(-2, 0)
    globalMin = min(-2, 0). # -2



"""