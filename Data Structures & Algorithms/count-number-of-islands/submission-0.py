class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        visit = set()

        def dfs(r, c):
            if r<0 or c<0 or r == ROWS or c == COLUMNS or (r, c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r, c))
            
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)


        numIslands = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    numIslands += 1
        return numIslands
                
