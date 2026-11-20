class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        def dfs(r, c, i):
            if len(word) == i:
                return True

            if r >= len(board) or r < 0 or c < 0 or c >= len(board[0]):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            tmp = board[r][c] 
            board[r][c] = '#'

            found = (dfs(r, c-1, i+1) or 
            dfs(r+1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r-1, c, i+1))

            board[r][c] = tmp

            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
                    
        return False


