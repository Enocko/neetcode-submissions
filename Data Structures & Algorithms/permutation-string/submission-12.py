class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        cntS1, cntS2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            cntS1[ord('a') - ord(s1[i])] += 1
            cntS2[ord('a') - ord(s2[i])] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if cntS1[i] == cntS2[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord('a') - ord(s2[r])
            cntS2[index] += 1
            if cntS1[index] == cntS2[index]:
                matches += 1
            elif cntS1[index]+1 == cntS2[index]:
                matches -= 1
            
            index = ord('a') - ord(s2[l])
            cntS2[index] -= 1
            if cntS1[index] == cntS2[index]:
                matches += 1
            elif cntS1[index]-1 == cntS2[index]:
                matches -= 1
                
            l += 1

        return matches == 26
        