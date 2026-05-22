class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ''

        for n in path + '/':
            if n == '/':
                if res == '..':
                    if stack: stack.pop()
                elif res != '.' and res != '':
                    stack.append(res)
                res = ''
            else:
                res += n
        
        return  '/' + '/'.join(stack)