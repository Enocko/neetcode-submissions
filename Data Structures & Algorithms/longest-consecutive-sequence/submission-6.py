class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        k = set(nums)
        res = 0

        for n in k:
            if (n-1) not in k:
                l = 0
                while (n+l) in k:
                    l += 1
                res = max(res, l)

        return res

        