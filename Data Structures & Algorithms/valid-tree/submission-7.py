class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        if n == 1:
            return True
            
        h = defaultdict(list)
        indegree = [0] * n

        for crs, pre in edges:
            h[crs].append(pre)
            h[pre].append(crs)
            indegree[pre] += 1
            indegree[crs] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            indegree[node] -= 1
            finish += 1
            
            for pre in h[node]:
                indegree[pre] -= 1
                if indegree[pre] == 1:
                    q.append(pre)
        
        return finish == n