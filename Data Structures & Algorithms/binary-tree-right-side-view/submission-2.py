# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            qlen = len(q)
            k = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    k = node
                    q.append(node.left)
                    q.append(node.right)
            if k:
                res.append(k.val)
        
        return res