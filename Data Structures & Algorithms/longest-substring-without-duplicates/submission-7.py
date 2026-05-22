class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        res = 0

        dist = 0
        i = 0
        while i < len(s):
            if s[i] in h and h[s[i]] >= dist:
                dist = 1 + h[s[i]]

            h[s[i]] = i
            res = max(res, i - dist + 1)
            i += 1
        
        return res