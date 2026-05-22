class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            h[crs].append(pre)
            indegree[pre] += 1
    
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
            