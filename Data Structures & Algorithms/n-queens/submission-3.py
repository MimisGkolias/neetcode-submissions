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

                



















        # res = []
        # cols, pos_diagonals, neg_diagonals = set(), set(), set()

        # def dfs(r, curr):
        #     if len(curr) == n:
        #         output = []
        #         for c in curr:
        #             output.append('.'*c + 'Q' + '.'*(n-c-1))
        #         res.append(output.copy())

        #         return
                
        #     for c in range(n):
        #         if (c in cols or
        #             (r+c) in pos_diagonals or
        #             (r-c) in neg_diagonals):
        #             continue
        #         else:
        #             cols.add(c)
        #             pos_diagonals.add(r+c)
        #             neg_diagonals.add(r-c)
        #             curr.append(c)

        #             dfs(r+1, curr)

        #             curr.pop()
        #             cols.remove(c)
        #             pos_diagonals.remove(r+c)
        #             neg_diagonals.remove(r-c)
            
        # dfs(0, [])
        # return res
                