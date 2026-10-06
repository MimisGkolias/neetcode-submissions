class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, x, y, result = [], 0, 0, 0
        operators = ['+', '-', '*', '/']

        for char in tokens:

            if char == '+':
                y = stack.pop()
                x = stack.pop()
                result = x + y
                stack.append(result)
            elif char == "-":
                y = stack.pop()
                x = stack.pop()
                result = x - y
                stack.append(result)
            elif char == "*":
                y = stack.pop()
                x = stack.pop()
                result = x * y
                stack.append(result)
            elif char == '/':
                y = stack.pop()
                x = stack.pop()
                result = int(x/y)
                stack.append(result)
            
            else:
                stack.append(int(char))
        return stack.pop()