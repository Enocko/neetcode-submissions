class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        for n in nums:
            if (n-1) not in nums:
                l = 0
                while (n+l) in nums:
                    l += 1
                longest = max(longest, l)
        
        return longest
