class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = nums[i]
                continue
            if i > 2:
                dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
            else:
                dp[i] = nums[i] + dp[i - 2]
        return max(dp[-1], dp[-2])
            