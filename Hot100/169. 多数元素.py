class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return nums
        mostShownNum = 0
        mostShownTime = 0
        nLen = len(nums)
        halfLen = nLen // 2
        for i in range(nLen):
            if mostShownTime == 0:
                mostShownNum = nums[i]
                mostShownTime += 1
            elif mostShownNum == nums[i]:
                mostShownTime += 1
                if mostShownTime > halfLen:
                    return mostShownNum
            else:
                mostShownTime -= 1
        return mostShownNum