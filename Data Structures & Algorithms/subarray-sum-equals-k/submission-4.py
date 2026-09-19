class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        res = 0
        curSum = 0

        for n in nums:
            h[curSum] += 1
            curSum += n
            res += h[curSum - k]
        
        return res



"""
{
    0: 1
    2: 2
   -1: 0
    1: 1
}

curSum = 4
res += 4
"""