class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                left = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sortedNums[i]:
                right = i
                break
        return 0 if right == left else right - left + 1