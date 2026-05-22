class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        l = len(strs)
        first = strs[0]
        last = strs[l-1]
        res = ''
        for i in range(len(min(first, last))):
            if first[i] != last[i]:
                break
            res += first[i]
        
        return res