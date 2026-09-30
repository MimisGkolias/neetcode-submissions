from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for char in s:
                arr[ord(char)-ord('a')] += 1
            hashMap[tuple(arr)].append(s)
        
        return list(hashMap.values())




        # res = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord("a")] += 1
        #     res[tuple(count)].append(s)
        # return list(res.values())

