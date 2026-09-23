import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashMap = defaultdict(int)
        t_hashMap = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            s_hashMap[char] += 1
        for char in t:
            t_hashMap[char] += 1

        return s_hashMap == t_hashMap


        # s_map = defaultdict(int)
        # t_map = defaultdict(int)

        # if len(s) != len(t):
        #     return False

        # for char in s:
        #     s_map[char] += 1
        # for char in t:
        #     t_map[char] += 1
        
        # return s_map == t_map

                