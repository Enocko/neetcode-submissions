# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while q:
            l = len(q)
            stack = []
            for i in range(l):
                node = q.popleft()
                if node:
                    stack.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if stack:
                res.append(stack.pop())
            
        return res