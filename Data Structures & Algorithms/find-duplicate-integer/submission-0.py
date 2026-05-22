class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            h[n] = 1 + h.get(n, 0)
        
        for k,v in h.items():
            if v >= 2:
                return k