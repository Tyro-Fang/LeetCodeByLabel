class Solution:
    def searchLeft(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        return start if nums[start] == target else end
    
    def searchRight(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        return end if nums[end] == target else start

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target == None:
            return[-1, -1]
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        if nums[left] != target:
            return[-1, -1]
        return [left, right]


