class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s.replace('()', '')
        #     s.replace('[]', '')
        #     s.replace('{}', '')
        
        # return s == ''

        stack = []
        h = {')': '(', ']': '[', '}': '{' }
        
        for c in s:
            if c in h:
                if stack and stack[-1] == h[c]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        