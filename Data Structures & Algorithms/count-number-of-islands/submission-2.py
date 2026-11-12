class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        visit = set()

        def dfs(r, c):
            if r<0 or c<0 or r == ROWS or c == COLUMNS or (r, c) in visit or grid[r][c] == "0":
                return False
            
            visit.add((r, c))
            
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            return True

        numIslands = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                    if dfs(r, c):
                        numIslands += 1
        return numIslands
                

    # BFS solution (Neetcode)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
