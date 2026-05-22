class Solution:
    def isPalindrome(self, s: str) -> bool:
        fin = ''
        for c in s:
            if c.isalnum():
                fin += c.lower()
        
        return fin == fin[:: -1]


        l, r = 0, len(s) - 1
        while l < r:
            while l < r and self.alphaNum(s[l]):
                l += 1
            while r > l and self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l = l + 1
            r = r - 1
        
        return True

    def alphaNum(self, c):
        ord('A') <= c <= ord('Z')
        ord('A') <= c <= ord('Z')
