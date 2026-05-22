class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {']': '[','}': '{',')': '('}

        for c in s:
            if c in h:
                if stack and h[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
    

# h = {']': '[',
#      '}': '{',
#      ')': '('}

# stack = []
# loop through s
# if c in h:
#     if stack and h[c] == stack[-1]
#         stack.pop()
#     else:
#         return False

# else:
#     stack.append('[')


# return len(stack) == 0