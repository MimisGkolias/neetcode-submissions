class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
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
            