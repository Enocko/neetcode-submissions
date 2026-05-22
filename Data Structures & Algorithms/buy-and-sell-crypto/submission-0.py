class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                k = prices[j] - prices[i]
                if k > 0:
                    res.append(k)
        
        if len(res) == 0:
            return 0
        else:

            return max(res)
        