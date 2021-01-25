class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        index = m + n - 1
        while ptr2 >= 0 and ptr1 >= 0:
            if nums2[ptr2] >= nums1[ptr1]:
                nums1[index] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[index] = nums1[ptr1]
                ptr1 -= 1
            index -= 1
        for i in range(ptr2 + 1):
            nums1[i] = nums2[i]

