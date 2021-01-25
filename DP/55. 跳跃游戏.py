# dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dp = [0] * len(nums)
        dp[0] = 1
        i = 0
        maxptr = 0
        while 1:
            if i >= len(nums) - 1:
                break
            if dp[i] == 1:
                tempMax = i + nums[i]
                if tempMax <= maxptr:
                    i += 1
                    continue
                else:
                    if tempMax >= len(nums) - 1:
                        return True
                    else:
                        maxptr = tempMax
                        for j in range(i, tempMax + 1):
                            dp[j] = 1
                i += 1
            else:
                i += 1
                continue
        return dp[len(nums) - 1] == 1
                    

#greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        maxPosition = 0
        for i, v in enumerate(nums):
            maxPosition = max(maxPosition, i + v)
            if maxPosition >= len(nums) - 1:
                return True
            if i >= maxPosition:
                return False