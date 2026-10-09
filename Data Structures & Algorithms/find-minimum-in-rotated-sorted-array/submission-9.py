class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1

        while l<=r:
            middle = l + (r-l)//2
            first_element = nums[middle]
            last_element = nums[(middle-1)%len(nums)]
            second_element = nums[(middle+1)%len(nums)]

            if first_element<last_element and first_element<=second_element:
                return nums[middle]

            elif first_element>=last_element and first_element<second_element:
                if first_element > nums[r]: 
                    l = middle + 1
                else:
                    r = middle - 1

            elif first_element>last_element and first_element>second_element:
                l = middle + 1
            
        
