class Solution:
    def isValid(self, s: str) -> bool:
        h = {')': '(', ']': '[', '}': '{'}
        stack = []
        for n in s:
            if n in h:
                if stack and stack[-1] == h[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        return len(stack) == 0
        