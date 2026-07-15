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
        while q: 
            node = q.popleft()
            res.append(node)
            for nei in h[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
    
        if len(res) == numCourses:
            return res[::-1]
        
        return []