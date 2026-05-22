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


        res = 0
        h = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            h[s[r]] = 1 + h.get(s[r], 0)
            maxf = max(maxf, h[s[r]])

            while (r-l+1) - maxf > k:
                h[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res


        