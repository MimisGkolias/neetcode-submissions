class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append([n for n in curr])
                return
            if total > target:
                return

            for index in range(i, len(nums)):
                curr.append(nums[index])
                dfs(index, curr, total + nums[index])
                curr.pop()

        dfs(0, [], 0)
        return res
