class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        # for n in strs:
        #     k = ''.join(sorted(n))
        #     h[k].append(n)
        # return list(h.values())
        

        for n in strs:
            count = [0]*26
            for c in n:
                count[ord(c) - ord('a')] += 1
            h[tuple(count)].append(n)
        
        return h.values()