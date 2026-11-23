class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, curr):
            if i == len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                l, r = i, j
                isPalindrome = True
                while l <= r:
                    if s[l] != s[r]:
                        isPalindrome = False
                        break
                    l += 1
                    r -= 1
                if isPalindrome:
                    curr.append(substring)
                    dfs(j+1, curr)
                    curr.pop()

        dfs(0, [])
        return res
    
                    
                