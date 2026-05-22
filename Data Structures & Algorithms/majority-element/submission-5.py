class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        c = 0
        for n in nums:
            if c == 0:
                res = n
            c += (1 if res == n else -1)
        return res