class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in matching_brackets.values():
                stack.append(char)
            else:
                if len(stack) != 0 and matching_brackets[char] != stack[-1]:
                    return False
                elif len(stack) != 0:
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False
                