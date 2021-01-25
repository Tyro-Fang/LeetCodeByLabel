#1.手动去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        nLen = len(nums)
        res = []
        def twoSum(startIndex, target):
            leftPtr = startIndex
            rightPtr = nLen - 1
            while leftPtr < rightPtr:
                if nums[leftPtr] + nums[rightPtr] == target:
                    res.append([-target, nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    while leftPtr < nLen and nums[leftPtr] == nums[leftPtr - 1]:
                        leftPtr += 1
                    rightPtr -= 1
                    while rightPtr > startIndex and nums[rightPtr] == nums[rightPtr + 1]:
                        rightPtr -= 1
                elif nums[leftPtr] + nums[rightPtr] < target:
                    leftPtr += 1
                    while leftPtr < nLen and nums[leftPtr] == nums[leftPtr - 1]:
                        leftPtr += 1
                else:
                    rightPtr -= 1
                    while rightPtr > startIndex and nums[rightPtr] == nums[rightPtr + 1]:
                        rightPtr -= 1

        for i in range(nLen - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twoSum(i + 1, -nums[i])
        return res        
        

#2.利用set去重