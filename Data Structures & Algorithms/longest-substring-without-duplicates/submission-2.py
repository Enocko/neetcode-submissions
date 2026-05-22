class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        pointer = 0
        i = 0
        res = 0
        while i < len(s):
            if s[i] in h and h[s[i]] >= pointer:
                pointer = h[s[i]] + 1
                h[s[i]] = i
            else:
                h[s[i]] = i
            res = max(res, i+1 - pointer)
            i += 1
        return res            
            

        