class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
         
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        hashset = set()
        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False