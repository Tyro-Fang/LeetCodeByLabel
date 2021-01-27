class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        state = 0
        def helper(nums, tempRes, res, lengs, state):
            if len(tempRes) == lengs:
                res.append(tempRes.copy())
                return
            for i in range(lengs):
                if ((state >> i) & 1) == 0:
                    tempRes.append(nums[i])
                    helper(nums, tempRes, res, lengs, state ^ (1 << i))
                    tempRes.pop(-1)
                else:
                    continue
        helper(nums, [], res, len(nums), state)
        return res
