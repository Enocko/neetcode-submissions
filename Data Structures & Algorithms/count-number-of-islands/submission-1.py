class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1,0], [-1,0], [0, 1], [0, -1]]
        islands = 0

        def dfs(i, j):
            if (i >= len(grid) or j >= len(grid[0]) or 
            i < 0 or j < 0 or grid[i][j]=='0'):
                return 0
            
            grid[i][j] = '0'
            for dr, dc in direction:
                dfs(i+dr, j+dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        
        return islands
