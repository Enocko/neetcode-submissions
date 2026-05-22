class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ''
        k = strs[0]
        j = strs[-1]
        for i in range(len(k)):
            if k[i] != j[i]:
                return res
            else:
                res += k[i]
        
        return res

