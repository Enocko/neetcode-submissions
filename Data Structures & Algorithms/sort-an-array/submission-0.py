class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        swap = True
        while swap:
            swap = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    swap = True
                    nums[i],nums[i+1] = nums[i+1], nums[i]
            
        return nums