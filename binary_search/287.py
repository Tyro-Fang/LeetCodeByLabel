def findDuplicate( nums) :
        if not nums:
            return -1
        numsLength = len(nums)
        start = 0
        end = numsLength -1
        while start + 1 < end:
            midNum = start + (end - start)  //2
            sumNums = 0
            for i in range(numsLength):
                if nums[i] <= midNum:
                    sumNums += 1
            if sumNums > midNum :
                end = midNum
            else :
                start = midNum + 1
        return start

a=[3,1,3,4,2]
print(findDuplicate(a))