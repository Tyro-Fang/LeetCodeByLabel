import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return nums
        maxValue = -sys.maxsize - 1
        tempval = 0
        for _, v in enumerate(nums):
            tempval = max(tempval + v, v)
            maxValue = max(tempval, maxValue)
        return maxValue