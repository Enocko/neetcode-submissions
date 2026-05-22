class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        h = defaultdict(int)
        for n in nums:
            h[n] += 1

        res = []
        stack = []

        def dfs():
            if len(stack) == len(nums):
                res.append(stack[:])
                return 

            for n in h:
                if h[n] > 0:
                    stack.append(n)
                    h[n] -= 1
                    dfs()

                    h[n] += 1
                    stack.pop()              
        
        dfs()
        return res


  