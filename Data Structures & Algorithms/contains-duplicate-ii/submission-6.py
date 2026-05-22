class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = defaultdict(int)

        for i, n in enumerate(nums):
            if n in h and abs(h[n] - i) <= k:
                return True
            h[n] = i
        
        return False