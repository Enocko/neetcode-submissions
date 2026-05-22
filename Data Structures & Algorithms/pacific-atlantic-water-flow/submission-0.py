class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visited, prevHeights):
            if (r >= len(heights) or c >= len(heights[0]) or
                r < 0 or c < 0 or (r, c) in visited 
                or heights[r][c] < prevHeights):
                return 
            
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res