class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l], nums[i] = nums[i], nums[l]
                c += 1
                l += 1
        
        return c
