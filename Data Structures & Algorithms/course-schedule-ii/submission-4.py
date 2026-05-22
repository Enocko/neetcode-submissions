class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        h = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            h[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            res.append(node)
            for pre in h[node]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        if finish == numCourses:
            return res[::-1]
        
        return []