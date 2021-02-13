class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return nums
        dpMax = dpMin = nums[0]
        maxValue = nums[0]
        for i in range(1, len(nums)):
            dpMax, dpMin = max(max(dpMax * nums[i], nums[i]), dpMin * nums[i]), min(min(dpMin * nums[i], nums[i]), dpMax * nums[i])
            maxValue = max(max(maxValue, dpMax), dpMin)
        return maxValue
                