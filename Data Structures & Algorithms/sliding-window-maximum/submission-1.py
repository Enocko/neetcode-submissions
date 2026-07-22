class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res
                


""".            
nums = [1,2,1,0,4,2,6]

output = [2, 2, 4, 4]
q = deque([6])

l = r = 0
while r < len(nums):
    
    while q and nums[q[-1]] < nums[r]:
        q.pop()
    
    q.append(r)

    if l > q[0]:
        q.popleft()

    if (r + 1) >= k:
        output.append(nums[q[0]])
        l +=  1
    
    r += 1


"""