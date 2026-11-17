class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(len(nums)):
                if nums[j] not in curr:
                    curr.append(nums[j])
                    dfs(j+1, curr)
                    curr.pop()

            return res
        dfs(0, [])
        return res