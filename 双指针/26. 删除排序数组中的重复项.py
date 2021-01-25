1.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 0
        sumNums = 0
        while index < len(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
                sumNums += 1
        return sumNums

2.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        left, right = 0, 1
        for _ in range(len(nums) - 1):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        
        return left + 1