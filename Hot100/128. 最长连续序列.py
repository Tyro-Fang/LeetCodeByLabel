class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = set(nums)
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] - 1 in numsSet:
                continue
            else:
                ans = 1
                start = nums[i] + 1
                while start in numsSet:
                    start += 1
                    ans += 1
                maxLen = max(ans, maxLen)
        return maxLen