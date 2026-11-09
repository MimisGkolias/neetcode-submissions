class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r-l)//2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # return -1




















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