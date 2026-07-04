class Solution:
    def intToRoman(self, num: int) -> str:
        list = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9],
                ['X', 10], ['XL', 40], ['L', 50], ['XC', 90],
                ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], 
                ['M', 1000]]
        
        res = ''
        for sym, val in list[::-1]:
            count = num // val
            if count:
                res += sym * count
                num = num % val
        
        return res



"""
num = 3749
res = ''

for x, y in list[::-1]:
    if 3749 // y:      #where y = 1000
        cnt = x * (3749 // y)
        res += cnt 
        num = 3749 % y  


"""