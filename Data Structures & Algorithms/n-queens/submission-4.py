class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, pos_diagonal, neg_diagonal = set(), set(), set()

        def dfs(r, curr):
            if r == n:
                res.append(['.'*c + 'Q' + '.'*(n-c-1) for c in curr])
                return
            
            for c in range(n):
                if (c in cols or
                    (r-c) in pos_diagonal or
                    (r+c) in neg_diagonal):
                    continue
                
                cols.add(c)
                pos_diagonal.add(r-c)
                neg_diagonal.add(r+c)
                curr.append(c)

                dfs(r+1, curr)

                cols.remove(c)
                pos_diagonal.remove(r-c)
                neg_diagonal.remove(r+c)
                curr.pop()

        dfs(0, [])
        return res          
                