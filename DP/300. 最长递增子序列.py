class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        maxSubSeq = 1
        dp[0] = 1
        for i in range(1, len(nums)):
            tempMax = 0
            for j in range(i):
                temp = 0
                if nums[j] >= nums[i]:
                    temp = 1
                else:
                    temp = dp[j] + 1
                if tempMax < temp:
                    tempMax = temp
            dp[i] = tempMax
            if maxSubSeq < tempMax:
                maxSubSeq = tempMax
        return maxSubSeq