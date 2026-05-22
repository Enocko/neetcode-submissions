class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for n in nums:
            h.add(n)
        
        return len(h) != len(nums)