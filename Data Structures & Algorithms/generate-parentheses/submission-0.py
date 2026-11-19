class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, usedOpen, usedClosed):
            if len(curr) == 2*n and usedOpen == n and usedClosed == n:
                res.append(''.join(curr))
                return
            if usedOpen > usedClosed:
                curr.append(")")
                dfs(curr, usedOpen, usedClosed+1)
                curr.pop()
            if usedOpen < n:
                curr.append("(")
                dfs(curr, usedOpen + 1, usedClosed)
                curr.pop()
            
        dfs([], 0, 0)
        return res