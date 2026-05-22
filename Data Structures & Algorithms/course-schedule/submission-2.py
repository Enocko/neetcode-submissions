class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        h = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[pre] += 1
            h[crs].append(pre)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1

            for pre in h[node]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return finish == numCourses
