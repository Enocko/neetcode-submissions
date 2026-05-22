class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = set()
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] - nums[i] == 1:
        #             res.add(nums[i])
        #             res.add(nums[j])
        # return len(res)



        numSet = set(nums)
        longest = 0

        for n in nums:
            
            if (n-1) not in numSet :
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
 
        