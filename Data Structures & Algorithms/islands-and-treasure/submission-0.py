class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        def addRoom(i, j):
            if (i >= len(grid) or j >= len(grid[0]) or
            i < 0 or j < 0 or grid[i][j]== -1 or (i, j) in visited):
                return 
            
            visited.add((i, j))
            q.append([i, j])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append([i, j])
        
        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist

                addRoom(i, j+1)
                addRoom(i, j-1)
                addRoom(i+1, j)
                addRoom(i-1, j)
            dist += 1
