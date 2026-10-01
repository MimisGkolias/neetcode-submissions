class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0]*26
        count = 0
        max_freq = 0

        l, r = 0, 0
        for r in range(len(s)):
            char = s[r]
            window[ord(char)-ord('A')] += 1
            max_freq = max(max_freq, window[ord(char)-ord('A')])

            if (r-l+1) - max_freq <= k and count < (r-l+1):
                count = (r-l+1)
            
            elif (r-l+1) - max_freq > k:
                window[ord(s[l])-ord('A')] -= 1
                l += 1

        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while r-l+1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res