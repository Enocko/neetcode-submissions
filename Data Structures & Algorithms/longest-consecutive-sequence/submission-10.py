class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        res = 0
        for n in h:
            if (n-1) not in h:
                l = 0
                while (n+l) in h:
                    l += 1
                    res = max(res, l)
        
        return res

        