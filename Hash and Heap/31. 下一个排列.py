class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        nLen = len(nums)
        ptr = nLen - 1
        startIndex = 0
        while ptr > 0:
            minIndex = 0
            maxNum = 999
            if nums[ptr] > nums[ptr - 1]:
                index = nLen - 1
                while index > ptr - 1:
                    if nums[index] > nums[ptr - 1] and nums[index] < maxNum:
                        maxNum = nums[index]
                        minIndex = index
                    index -= 1
                if maxNum < 999:
                    nums[ptr - 1], nums[minIndex] = nums[minIndex], nums[ptr - 1]
                    startIndex = ptr
                    break           
            ptr -= 1
        endIndex = nLen - 1
        while startIndex < endIndex:
            nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
            startIndex += 1
            endIndex -= 1
        return

