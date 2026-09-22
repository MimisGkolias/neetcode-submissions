import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            s_map[char] += 1
        for char in t:
            t_map[char] += 1
        
        for key, value in s_map.items():
            if t_map[key] != value:
                return False
        return True

                