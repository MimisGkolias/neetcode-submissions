class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while (r-l) > 0:
            middle = l + (r-l)//2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                r = middle
            elif target > nums[middle]:
                l = middle + 1
        
        return -1