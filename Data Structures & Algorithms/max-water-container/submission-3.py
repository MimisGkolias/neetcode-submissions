class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l <= r:
            container = (min(heights[l], heights[r])*(r-l))
            if res < container:
                res = container
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l, res = 0, 0
        # r = len(heights) - 1
        
        # while l < r:
        #     if res > ((r-l)*min(heights[l], heights[r])):
        #         if min(heights[l], heights[r]) == heights[l]:
        #             l += 1
        #         else:
        #             r -= 1
        #         continue
        #     else:
        #         res = ((r-l)*min(heights[l], heights[r]))
        #         if min(heights[l], heights[r]) == heights[l]:
        #             l += 1
        #         else:
        #             r -= 1
        # return res