class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(m):
            subarrays, canCurr = 1, m
            for n in nums:
                if canCurr - n < 0:
                    subarrays += 1
                    canCurr = m

                canCurr -= n
            
            return subarrays <= k

        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

