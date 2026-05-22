class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ship, currCap = 1, cap
            for n in weights:
                if currCap - n < 0:
                    ship += 1
                    currCap = cap
                currCap -= n 
            return ship <= days

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res