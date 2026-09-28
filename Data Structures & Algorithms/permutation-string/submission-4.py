from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        hashMap1 = defaultdict(int)
        hashMap2 = defaultdict(int)

        for char in s1:
           hashMap1[(ord(char)-ord('a'))] += 1
        for i in range(len(s1)):
            hashMap2[(ord(s2[i]))-ord('a')] += 1
        

        for r in range(len(s1), len(s2)):
            if hashMap1 == hashMap2:
                return True
            else:
                hashMap2[(ord(s2[r]) - ord('a'))] += 1
                hashMap2[(ord(s2[l]) - ord('a'))] -= 1
                
                if hashMap2[(ord(s2[l]) - ord('a'))] == 0:
                    del hashMap2[(ord(s2[l]) - ord('a'))]
                l += 1            
        return hashMap1 == hashMap2