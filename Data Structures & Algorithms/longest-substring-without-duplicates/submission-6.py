class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        res = 0
        i = 0
        pointer = 0 

        while i < len(s):
            if s[i] in h and h[s[i]] >= pointer:
                pointer = h[s[i]] + 1
                h[s[i]] = i
            else:
                h[s[i]] = i

            res = max(res, i-pointer + 1)
            i += 1
        
        return res
