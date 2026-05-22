class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h ={}
        res = 0
        i = 0
        pointer = 0
        while i < len(s):
            if s[i] in h and h[s[i]] >= pointer:
                pointer = h[s[i]] + 1
                h[s[i]] = i
            
            else:
                res = max(res, i+1 - pointer)
                h[s[i]] = i
            i += 1
            
        return res
                
        