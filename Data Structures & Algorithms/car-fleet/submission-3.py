class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        data = list(zip(position, speed))
        data.sort()
        times = [(target-data[i][0])/data[i][1] for i in range(len(data))]

        for i in range(len(times)-1, -1, -1):
            if not stack or times[i] > stack[-1]:
                stack.append(times[i])
        return len(stack)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack, current_time = [], 0
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for pos, sp in cars:
            current_time = ((target - pos)/sp)
        
            if not stack or current_time > stack[-1]:
                stack.append(current_time)
            else:
                continue
        return len(stack)
            