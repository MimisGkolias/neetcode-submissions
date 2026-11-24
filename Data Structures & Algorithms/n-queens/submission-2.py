class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, pos_diagonals, neg_diagonals = set(), set(), set()

        def dfs(r, curr):
            if len(curr) == n:
                output = []
                for c in curr:
                    output.append('.'*c + 'Q' + '.'*(n-c-1))
                res.append(output.copy())

                return
                
            for c in range(n):
                if (c in cols or
                    (r+c) in pos_diagonals or
                    (r-c) in neg_diagonals):
                    continue
                else:
                    cols.add(c)
                    pos_diagonals.add(r+c)
                    neg_diagonals.add(r-c)
                    curr.append(c)

                    dfs(r+1, curr)

                    curr.pop()
                    cols.remove(c)
                    pos_diagonals.remove(r+c)
                    neg_diagonals.remove(r-c)
            
        dfs(0, [])
        return res
                