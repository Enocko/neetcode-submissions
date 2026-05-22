
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        # for word in strs:
        #     k = " ".join(sorted(word))
        #     h[k].append(word)        
        # return list(h.values())

    
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            h[tuple(count)].append(word)
        
        return h.values()
            
            