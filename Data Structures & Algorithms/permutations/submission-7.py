class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                curr.append(nums[i])
                used.add(nums[i])
                dfs(curr)
                curr.pop()
                used.remove(nums[i])
            return res
        dfs([])
        return res





















        # res = []
        # used = set()

        # def dfs(curr):
        #     if len(curr) == len(nums):
        #         res.append(curr.copy())
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] in used:
        #             continue
            
        #         curr.append(nums[i])
        #         used.add(nums[i])
        #         dfs(curr)
        #         curr.pop()
        #         used.remove(nums[i])

        #     return res
        # dfs([])
        # return res