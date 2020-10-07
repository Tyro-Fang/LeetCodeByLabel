class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        isNums1Less=False
        if nums1Length < nums2Length:
            isNums1Less = True
        if isNums1Less:
            nums1.sort()
        else:
            nums2.sort()
        result=set()
        if isNums1Less:
            sortedNums=nums1
            searchNums=nums2
        else:
            sortedNums=nums2
            searchNums=nums1
        
        for i in range(len(searchNums)):
            if self.binarySearch(sortedNums,searchNums[i]):
                result.add(searchNums[i])
        return result

        
    def binarySearch(self,nums, target):
        numsLength = len(nums)
        start = 0
        end = numsLength - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False