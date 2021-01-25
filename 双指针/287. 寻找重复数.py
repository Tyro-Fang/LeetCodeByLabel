class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return  0
        n = len(nums) - 1
        mid = n // 2
        left = 0
        right = n 
        while left < right:
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid 
            mid = (left + right ) // 2

        return left