class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0]*len(temperatures)
        if len(temperatures) == 1:
            return [0]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
            else:
                stack.append((temperatures[i], i))
        return res            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                element = stack.pop()
                result[element] = (i - element)

            stack.append(i)
        return result