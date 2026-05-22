class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        res = x + y
        
        return bin(res)[2:]