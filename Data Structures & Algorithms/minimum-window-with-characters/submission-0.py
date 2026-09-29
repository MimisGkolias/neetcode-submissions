from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        window = {}
        tMap = {}
        res, resLen = [-1, -1], float("infinity")
        
        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)
        
        have, need = 0, len(tMap)

        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                
                l += 1
            
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""




