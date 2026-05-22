class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = defaultdict(int)
        for n in nums:
            h[n] += 1
            if h[n] >= 2:
                return n
        
