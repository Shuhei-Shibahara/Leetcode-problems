class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            preims = dfs(i+1,j)
            preims += dfs(i, j+1)
            preims += dfs(i-1,j)
            preims += dfs(i, j-1)
            return preims
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
        
            