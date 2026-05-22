class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        countT = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1


        
        l, r = res
        return s[l : r+1] if resLen != float('inf') else ''




"""
countT = {
    X: 1,
    Y: 1,
    Z: 1
    }
need = 3

window = {
    O: 1,
    U: 1,
    Z: 1,
    D: 1,
    Y: 1,
    X: 1
}
have = 3
while have == need:
    res = [0, 6]
    resLen = 7

    l += 1
"""
