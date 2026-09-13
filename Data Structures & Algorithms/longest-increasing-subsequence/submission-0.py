class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


"""
LIS = [1, 1, 1, 1, 1, 1, 1,]

LIS =   [2, 2, 4, 3, 3, 2, 1,   1]
         0  1  2  3  4  5   6   7
nums = [10, 9, 2, 5, 3, 7, 101, 18]

for i in range(len(nums)-1, -1, -1):   # 0
    for j in range(i+1, len(nums)): # 1
        if nums[i] < nums[j]:
            LIS[i] = max(LIS[i], 1 + LIS[j])

return max(LIS)


"""
