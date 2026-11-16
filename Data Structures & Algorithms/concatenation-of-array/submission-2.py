class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0]*2*len(nums)
        
        for i in range(len(nums)):
            res[i] = nums[i]
        for i in range(len(nums)):
            res[len(nums)+i] = nums[i]
        return res




















        ans = [0]*2*len(nums)
        for i in range(len(nums)):
            ans[i]=nums[i]
        for i in range(len(nums), 2*len(nums)):
            ans[i] = nums[i-len(nums)]
        return ans