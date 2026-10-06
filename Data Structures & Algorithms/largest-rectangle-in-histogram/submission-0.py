class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
