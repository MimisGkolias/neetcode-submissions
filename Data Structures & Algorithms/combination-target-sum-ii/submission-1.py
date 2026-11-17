class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            elif total > target:
                return
            else:
                for i in range(i, len(nums)):
                    curr.append(nums[i])
                    dfs(i+1, curr, total + nums[i])
                    curr.pop()
                    while i>0 and nums[i] == nums[i-1]:
                        continue
            dfs(0, [], 0)
            return res





























        res = []
        candidates.sort()
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            elif total > target:
                return 
            else:
                for j in range(i, len(candidates)):
                    if j > i and candidates[j] == candidates[j-1]:
                        continue
                    curr.append(candidates[j])
                    dfs(j+1, curr, total + candidates[j])
                    curr.pop()
            return res
        
        dfs(0, [], 0)
        return res
