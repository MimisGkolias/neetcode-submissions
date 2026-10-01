class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in matching_brackets.values():
                stack.append(char)
            elif not stack or matching_brackets[char] != stack.pop():
                return False
                
        return not stack
                