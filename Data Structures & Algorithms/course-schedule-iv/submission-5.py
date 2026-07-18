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
        
        res = defaultdict(set)
        while q:
            node = q.popleft()
            for nei in h[node]:
                res[nei].add(node)
                res[nei].update(res[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return [u in res[v] for u, v in queries]


"""
0 -> 1 - > 2 -> 3
h = {
    1: [0]
    2: [1]
    3: [2]
}
indegree = [1, 1, 1, 0]
q = [3]
"""