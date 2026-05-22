class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:  
        h = {}
        
        for i, t in enumerate(nums):
            if t in h and abs(h[t]-i) <= k:
                    return True
            
            h[t] = i
    
        return False
            
