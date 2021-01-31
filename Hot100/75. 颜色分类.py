class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(nums, start, end):
            if start == end:
                return 
            left = start + 1
            right = end
            while True:
                while nums[left] < nums[start]:
                    if left == end:
                        break
                    left += 1
                while nums[right] > nums[start]:
                    if right == start:
                        break
                    right -= 1
                if left >= right:
                    break
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            nums[right], nums[start] = nums[start], nums[right]
            return right
        def quickSort(nums, start, end):
            if start >= end:
                return 
            mid = helper(nums, start, end)
            quickSort(nums, start, mid - 1)
            quickSort(nums, mid + 1, end)
        quickSort(nums, 0, len(nums) - 1)
        