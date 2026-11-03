class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea























        max_area, stack = 0, []
        heights.append(0)

        for i, height in enumerate(heights):
            start = i
            while stack and heights[i] <stack[-1][0]:
                popped_height, j = stack.pop()
                max_area = max(max_area, popped_height*(i-j))
                start = j
            stack.append((height, start))

        while stack:
            popped_height, j = stack.pop()
            max_area = max(max_area, popped_height*(len(heights)-j))
        return max_area
