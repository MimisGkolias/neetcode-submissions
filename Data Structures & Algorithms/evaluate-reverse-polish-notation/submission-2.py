class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(token))  
        
        return stack[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack, x, y, result = [], 0, 0, 0
        # operators = ['+', '-', '*', '/']

        # for char in tokens:

        #     if char == '+':
        #         y = stack.pop()
        #         x = stack.pop()
        #         result = x + y
        #         stack.append(result)
        #     elif char == "-":
        #         y = stack.pop()
        #         x = stack.pop()
        #         result = x - y
        #         stack.append(result)
        #     elif char == "*":
        #         y = stack.pop()
        #         x = stack.pop()
        #         result = x * y
        #         stack.append(result)
        #     elif char == '/':
        #         y = stack.pop()
        #         x = stack.pop()
        #         result = int(x/y)
        #         stack.append(result)
            
        #     else:
        #         stack.append(int(char))
        # return stack.pop()