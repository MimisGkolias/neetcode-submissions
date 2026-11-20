class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, usedLeft, usedRight):
            if usedLeft == n and usedRight == n:
                res.append(''.join(curr))
                return
            
            if usedLeft < n:
                curr.append('(')
                dfs(curr, usedLeft + 1, usedRight)
                curr.pop()
            if usedLeft > usedRight:
                curr.append(')')
                dfs(curr, usedLeft, usedRight + 1)
                curr.pop()
            return res
        dfs([], 0, 0)
        return res
