class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack, time = [], []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for pos, sp in cars:
            time.append((target - pos)/sp)
        
        for i in range(len(time)):
            if not stack or time[i] > stack[-1]:
                stack.append(time[i])
            else:
                continue
        return len(stack)
            