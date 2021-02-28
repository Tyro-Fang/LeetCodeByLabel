class Solution:
    def quickSort(self, nums):
        self.sort(nums, 0, len(nums) - 1)

    def partition(self, nums, start, end):
        left = start + 1
        right = end
        num = nums[start]
        while True:
            while  nums[left] < num:
                left += 1
                if left == end:
                    break
            while nums[right] > num:
                right -= 1
                if right == start:
                    break
            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]
        return right
    
    def sort(self, nums, start, end):
        if start >= end:
            return
        partition = self.partition(nums, start, end)
        self.sort(nums,start, partition - 1)
        self.sort(nums, partition + 1, end)

a = [1,3,5,7,3,2,5,7]
x = Solution()
x.quickSort(a)
print(a)