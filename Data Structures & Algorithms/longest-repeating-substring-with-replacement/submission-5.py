class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # h = defaultdict(int)
        # for n in s:
        #     h[n] += 1
        # s = 0
        # for c in h.values():
        #     if s < c:
        #         s = c
        
        # return s+k



        h = {}
        maxf = 0
        l = 0
        res = 0
        for i in range(len(s)):
            h[s[i]] = 1 + h.get(s[i], 0)
            maxf = max(maxf, h[s[i]])
        
            while (i+1-l) - maxf > k:
                h[s[l]] -= 1
                l += 1
        res = max(res, i+1-l)

        return res