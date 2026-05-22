class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)

        for n in nums:
            h[n] += 1
            if len(h) <= 2:
                continue
            
            cnt = defaultdict(int)
            for k, v in h.items():
                v -= 1
                cnt[k] = v
                h = cnt
        
        res = []
        for n in h:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res