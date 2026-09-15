class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for n in dp:
                nextDp.add(n + nums[i])
                nextDp.add(n)
            dp = nextDp
        
        return target in dp