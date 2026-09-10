class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 0:
        #     return 0
        
        # if n == 1 or n == 2:
        #     return 1 
        
        # return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        # h = {}
        # def dfs(n):
        #     if n in h:
        #         return h[n]
            
        #     if n == 0:
        #         h[n] = 0

        #     elif n == 1 or n == 2:
        #         h[n] = 1
            
        #     else:
        #         h[n] = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)

        #     return h[n]
        # return dfs(n)

        if n <= 2:
            return 1 if n != 0 else 0

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]
        
        return dp[n]