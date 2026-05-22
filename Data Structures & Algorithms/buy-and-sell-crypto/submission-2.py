class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = []
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         k = prices[j] - prices[i]
        #         if k > 0:
        #             res.append(k)
        
        # if len(res) == 0:
        #     return 0
        # else:

        #     return max(res)


        l, r = 0, 1
        m = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                m = max(m, profit)
            else:
                l = r
            r += 1
        
        return m
        