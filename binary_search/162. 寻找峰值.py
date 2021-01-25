class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        nLen = len(nums)
        left = 0
        right = nLen - 1
        def isBigger(index1, index2):
            if index2 == -1 or index2 == nLen or nums[index1] > nums[index2]:
                return True
            return False
        while left < right:
            mid = left + (right - left) // 2
            if isBigger(mid, mid - 1) and isBigger(mid, mid + 1):
                return mid
            elif isBigger(mid, mid - 1):
                left = mid + 1
            else:
                right = mid 
        if isBigger(left, left - 1) and isBigger(left, left + 1):
            return left
        return left