class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]
        res = ''
        for i in range(len(first)):
            if first[i] == last[i]:
                res += first[i]
            else:
                return res
            
        return res