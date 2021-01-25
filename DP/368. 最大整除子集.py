#1.dp
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return [-1, -1]
        nums.sort()
        dp = [[]] * len(nums)
        
        dp[0] = [nums[0]]
        res = [nums[0]]
        for i in range(1, len(nums)):
            maxArray = [nums[i]]
            maxLen = 1
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    tempLen = len(dp[j]) + 1
                    if tempLen > maxLen:
                        maxLen = tempLen
                        maxArray = dp[j].copy()
                        maxArray.append(nums[i])
                else:
                    continue
            dp[i] = maxArray
            if len(res) < maxLen:
                res = maxArray
        return res

#2。dp加上空间优化
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return [-1, -1]
        nums.sort()
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0] = [1, -1]
        allMaxVal = 1
        allMaxPtr = 0
        for i in range(1, len(nums)):
            maxVal= i
            maxLen = 1
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    tempLen = dp[j][0] + 1
                    if tempLen > maxLen:
                        maxLen = tempLen
                        maxVal = j
                else:
                    continue
            dp[i] = [maxLen, maxVal]
            if allMaxVal < maxLen:
                allMaxVal = maxLen
                allMaxPtr = i
        res = []
        i = allMaxPtr
        #return allMaxPtr
        while i >= 0:
            res.append(nums[i])
            i = dp[i][1]
            if i == dp[i][1]:
                if i >= 0:
                    res.append(nums[i])
                break
        res.reverse()
        return res


