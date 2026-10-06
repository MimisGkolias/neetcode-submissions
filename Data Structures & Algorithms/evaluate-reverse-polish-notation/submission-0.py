class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, x, y, result = [], 0, 0, 0
        operators = ['+', '-', '*', '/']

        for char in tokens:
            if char in operators and len(stack) > 1:
                y = stack.pop()
                x = stack.pop()
                if char == '+':
                    result = x + y
                elif char == "-":
                    result = x - y
                elif char == "*":
                    result = x * y
                else:
                    result = int(x/y)
                    
                stack.append(result)
            else:
                stack.append(int(char))
        return stack.pop()