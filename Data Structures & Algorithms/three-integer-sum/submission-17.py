class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    # r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res




















        res = []
        nums.sort()

        
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res


        
                
        # q = 0 
        # res, checkSum = set(), 0

        # nums.sort()

        # for q in range(len(nums)):
        #     l, r = q + 1, len(nums) - 1
        #     while l < r:
        #         checkSum = nums[q] + nums[l] + nums[r]
        #         if checkSum == 0:
        #             res.add(tuple([nums[q], nums[l], nums[r]]))
        #             l += 1
        #         elif checkSum > 0:
        #             r -= 1
        #         elif checkSum < 0:
        #             l += 1
        # return list(res)


            
        