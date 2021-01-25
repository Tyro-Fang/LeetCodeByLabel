class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthNumber(k):
            index1 = 0
            index2 = 0
            while True:
                if index1 == n1Len:
                    return nums2[index2 + k - 1]
                if index2 == n2Len:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                #正常情况下二分查找
                p = k // 2
                #防止越界
                newIndex1 = min(index1 + p - 1, n1Len - 1)
                newIndex2 = min(index2 + p - 1, n2Len - 1)
                if nums1[newIndex1] <= nums2[newIndex2]:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        n1Len = len(nums1)
        n2Len = len(nums2)
        total = n1Len + n2Len
        if total % 2 == 0:
            return (getKthNumber(total // 2) + getKthNumber(total // 2 + 1)) / 2
        else:
            return getKthNumber((total + 1) // 2)


