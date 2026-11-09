class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # More optimal
        if len(s) == 0:
            return 0
        res = 0
        hashMap = {}
        l = 0

        for r in range(len(s)):
            current_char = s[r]
            
            if current_char in hashMap and hashMap[current_char] >= l:
                l = hashMap[current_char] + 1
            
            hashMap[current_char] = r
            res = max(res, r - l + 1)
        return res



        # With a set
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



        # O(n), O(n)
        if len(s) == 0:
            return 0

        res = 0
        hashMap = {}
        l, r = 0, 0

        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            while hashMap[s[r]] > 1:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


                

