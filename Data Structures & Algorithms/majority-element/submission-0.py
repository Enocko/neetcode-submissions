class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            h[n] = 1 + h.get(n, 0)
            if h[n] > len(nums)/2:
                return n