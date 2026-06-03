class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(m):
            ship, curr = 1, m
            for w in weights:
                if curr - w < 0:
                    ship += 1
                    curr = m
                curr -= w
            
            return ship <= days

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res



"""
l, r = 10, 26
m = 18

def canShip(m):
    ship = 1, curr = 18
    for w in weights:
        if curr - w < 0:
            ship += 1
            curr = 18
        curr -= w

while l <= r:
     m = (l + r) // 2
    if canShip(m):
        res = min(res, m)
        r = m - 1
    else:
        l = m + 1



"""
