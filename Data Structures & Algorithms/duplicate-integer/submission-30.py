class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        # for n in nums:
        #     if n in h:
        #         return True
        #     h.add(n)
        # return False

        for n in nums:
            h.add(n)
        
        if len(h) == len(nums):
            return False
        return True
  