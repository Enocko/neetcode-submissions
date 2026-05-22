class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)

        for n in nums:
            h[n] += 1
            if len(h) < 3:
                continue
            
            new_cnt = defaultdict(int)
            for k, v in h.items():
                if v > 1:
                    new_cnt[k] = v - 1
                h = new_cnt
            
        
        res = []
        for n in h:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res