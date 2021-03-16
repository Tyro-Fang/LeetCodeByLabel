class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return nums
        sumVal = 0
        for num in nums:
            sumVal += num
        if sumVal < S:
            return 0
        t = 2 * sumVal + 1
        dp = [[0] * t for _ in range(len(nums))]
        
        if nums[0] == 0:
            dp[0][sumVal] = 2
        else:
            dp[0][nums[0] + sumVal] = 1
            dp[0][sumVal - nums[0]] = 1
        for i in range(1, len(nums)):
            for j in range(2 * sumVal + 1):
                addVal = j + nums[i] if j + nums[i] < (2 *sumVal + 1) else 0
                minuVal = j - nums[i] if j - nums[i] >=0 else 0
                dp[i][j] = dp[i - 1][addVal] + dp[i - 1][minuVal]
        return dp[-1][S + sumVal]
