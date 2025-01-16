class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #first find the island using dfs
        #then use bfs to find the shortest bridge

        N = len(grid)
        direct = [[0,1],[1,0],[0,-1],[-1,0]]
        def inValid(r,c):
            return r < 0 or c < 0 or r == N or c == N
                
        visit = set()
        
        def dfs(r,c):
            if (inValid(r,c) or grid[r][c] == 0 or (r,c) in visit):
                return
            visit.add((r,c))
            for dr,dc in direct:
                dfs(r+dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in direct:
                        curR, curC = r + dr, c + dc
                        if inValid(curR, curC) or (curR,curC) in visit:
                            continue
                        if grid[curR][curC] == 1:
                            return res
                        q.append([curR,curC])
                        visit.add((curR,curC))
                res += 1
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return bfs()
        