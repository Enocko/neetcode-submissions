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
    
        visited = set()
        while q:
            node = q.popleft()
            visited.add(node)
            for nei in h[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return len(visited) == numCourses

"""
h = {
    0: 1
}

indegree = [0, 1]
"""