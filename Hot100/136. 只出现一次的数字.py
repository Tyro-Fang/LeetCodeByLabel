class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res
