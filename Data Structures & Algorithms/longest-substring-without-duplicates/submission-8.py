class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        i = 0
        point = 0
        res = 0

        for i in range(len(s)):
            if s[i] in h and h[s[i]] >= point:
                point = h[s[i]] + 1
            
            h[s[i]] = i
            res = max(res, i - point + 1)
        
        return res
