class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visit = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r, c):
            if (r,c) in visit or r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        island_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visit:
                    dfs(i, j)
                    island_count += 1
        
        return island_count
