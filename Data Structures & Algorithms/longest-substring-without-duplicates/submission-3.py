class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 0
        hashMap = {}
        l, r = 0, 0

        while r < len(s):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            while hashMap[s[r]] > 1:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res






















        l = 0
        charSet = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
                

