class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict(int)
        maxf = 0
        l = 0
        res = 0

        for i in range(len(s)):
            h[s[i]] += 1
            maxf = max(maxf, h.get(s[i], 0))

            while (i - l + 1) - maxf > k:
                h[s[l]] -= 1
                l += 1
            
            res = max(res, i - l + 1)
        
        return res
