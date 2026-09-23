class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ("".join(char for char in s if char.isalnum())).lower()
        l = 0
        r = len(clean_text)-1
        print(clean_text)
        while l < r:
            if clean_text[l] != clean_text[r]:
                return False
            l += 1
            r -= 1
        return True
       