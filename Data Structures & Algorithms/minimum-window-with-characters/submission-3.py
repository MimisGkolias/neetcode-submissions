from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        l, r = 0, 0
        res = []
        window_count, target_count = 0, 0
        window_Map, t_Map = {}, {}

        for char in t:
            t_Map[char] = 1 + t_Map.get(char, 0)
        target_count = len(t_Map)

        for r in range(len(s)):
            window_Map[s[r]] = 1 + window_Map.get(s[r], 0)
            if s[r] in t_Map and window_Map[s[r]] == t_Map[s[r]]:
                window_count += 1

            while window_count == target_count:
                if len(res) == 0 or (res[1]-res[0]) > (r-l):
                    res = [l, r]
                window_Map[s[l]] -= 1
                
                if s[l] in t_Map and window_Map[s[l]] < t_Map[s[l]]:
                    window_count -= 1

                l += 1
        return s[res[0]:res[1]+1] if len(res) > 0 else ""            
        
        
        
        
        
        # if len(t) > len(s) or t == "":
        #     return ""
        
        # window = {}
        # tMap = {}
        # res, resLen = [-1, -1], float("infinity")
        
        # for char in t:
        #     tMap[char] = 1 + tMap.get(char, 0)
        
        # have, need = 0, len(tMap)

        # l=0
        # for r in range(len(s)):
        #     window[s[r]] = 1 + window.get(s[r], 0)

        #     if s[r] in tMap and window[s[r]] == tMap[s[r]]:
        #         have += 1
            
        #     while have == need:
        #         if (r-l+1) < resLen:
        #             res = [l,r]
        #             resLen = r-l+1

        #         window[s[l]] -= 1
        #         if s[l] in tMap and window[s[l]] < tMap[s[l]]:
        #             have -= 1
                
        #         l += 1
            
        # l,r = res
        # return s[l:r+1] if resLen != float('infinity') else ""




