class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        if nums[end] > nums[start]:
            return nums[start]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

