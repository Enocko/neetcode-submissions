class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[ : i] + digit + lock[i+1: ])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[: i] + digit + lock[i+1: ])
            return res

        visited = set(deadends)
        q = deque([('0000', 0)])
        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn 
            for x in children(lock):
                if x not in visited:
                    visited.add(x)
                    q.append([x, turn + 1])
        
        return -1
