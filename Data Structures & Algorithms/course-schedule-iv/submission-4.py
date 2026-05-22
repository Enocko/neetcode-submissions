class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        h = defaultdict(list)
        indegree = [0] * numCourses
        for pre, crs in prerequisites:
            h[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)


        dict = defaultdict(set)
        while q:
            node = q.popleft()
            for nei in h[node]:
                dict[nei].add(node)
                dict[nei].update(dict[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return [u in dict[v] for u, v in queries]
        



