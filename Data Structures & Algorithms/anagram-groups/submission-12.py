class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for n in strs:
            k = ''.join(sorted(n))
            h[k].append(n)
        return h.values()