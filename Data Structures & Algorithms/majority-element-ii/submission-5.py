class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = Counter(nums)
        
        res = []
        for k, v in h.items():
            if v > len(nums)/3:
                res.append(k)
        
        if not res:
            return []
        
        return res