class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target == None:
            return []
        candidates.sort()
        res = []
        def helper(candidates, index, target, tempRes):
            if target == 0:
                res.append(tempRes.copy())
                return
            for i in range(index, len(candidates)):
                target = target - candidates[i]
                if target < 0:
                    break
                tempRes.append(candidates[i])
                helper(candidates, i, target, tempRes)
                tempRes.pop(-1)
                target += candidates[i]
        helper(candidates, 0, target, [])
        return res