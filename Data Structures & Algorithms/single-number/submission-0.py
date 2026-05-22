class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = defaultdict(int)
        for n in nums:
            h[n] += 1
        
        for k,v in h.items():
            if v == 1:
                return k