class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                i, j = q.popleft()

                for dr, dc in direction:
                    row, col = i+dr, j+dc

                    if (row >= len(grid) or col >= len(grid[0]) or
                    row < 0 or col < 0 or grid[row][col] != 1):
                        continue
                    
                    q.append([row, col])
                    grid[row][col] = 2
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
