def findMedianSortedArrays(nums1, nums2):
        if  nums1 ==None or nums2 == None:
            return -1
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        sumLength = nums1Length + nums2Length
        isSumOdd = False
        if sumLength % 2 != 0:
            isSumOdd = True
        medianNum = sumLength // 2
        halfSearchNum = medianNum // 2
        while medianNum > 1 or nums1 != [] or nums2 != []:
            if nums1[halfSearchNum] > nums2[halfSearchNum]:
                nums2 = nums2[halfSearchNum:]
            else: 
                nums1=nums1[halfSearchNum:]
            medianNum -= halfSearchNum
            halfSearchNum = medianNum // 2
        res = 0
        if nums1 == []:
            res = nums2[medianNum]
        elif nums2 == []:
            res =nums1[medianNum]
        elif nums1[0] < nums2[0]:
            res = nums2[0]
            nums2 = nums2[1:]
        else:
            res = nums1[0]
            nums1 = nums1[1:]
        if not isSumOdd:
            if nums1 == []:
                res+= nums2[0]
            elif  nums2 == []:
                res+= nums1[0]
            elif nums1[0] < nums2[0]:
                res += nums2[0]
            else:
                res += nums1[0]
            res /= 2
        return res
a = [0,0,0,0,0]
b = [-1,0,0,0,0,0,1]
print(findMedianSortedArrays(a,b))