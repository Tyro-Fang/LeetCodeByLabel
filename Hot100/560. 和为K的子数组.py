class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return nums
        dicts = {0:1}
        count, preSum = 0, 0
        for i in range(len(nums)):
            preSum += nums[i]
            if (preSum - k) in dicts:
                count += dicts[(preSum - k)]
            if preSum in dicts:
                dicts[preSum] += 1
            else:
                dicts[preSum] = 1
        return count