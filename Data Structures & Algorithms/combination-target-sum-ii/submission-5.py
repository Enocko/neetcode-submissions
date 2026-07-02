class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        stack = []

        def dfs(i):
            if sum(stack) == target:
                res.append(stack[:])
                return 
            
            if i >= len(candidates) or sum(stack) > target:
                return 
            
            stack.append(candidates[i])
            dfs(i+1)

            stack.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res

