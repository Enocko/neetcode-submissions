class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i,n in enumerate(nums):
            if n in h and abs(i - h[n]) <= k:
                return True
            else:
                h[n] = i
        
        return False