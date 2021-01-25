class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or  target == None or len(nums) < 4:
            return []
        nums.sort()
        nLen = len(nums)
        res = []
        for i in range(nLen - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            maxValue = nums[i] + nums[-1] + nums[-2] + nums[-3]
            minValue = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if maxValue < target:
                continue
            if minValue > target:
                break
            for j in range(i + 1, nLen - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                maxValue = nums[i] + nums[j] + nums[-1] + nums[-2]
                minValue = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if maxValue < target:
                    continue
                if minValue > target:
                    break
                leftPtr = j + 1
                rightPtr = nLen - 1
                while leftPtr < rightPtr:
                    temp =  nums[i] + nums[j] + nums[leftPtr] + nums[rightPtr]
                    if temp == target:
                        res.append([nums[i], nums[j], nums[leftPtr],  nums[rightPtr]])
                        leftPtr += 1
                        while leftPtr < nLen and nums[leftPtr] == nums[leftPtr - 1]:
                            leftPtr += 1
                        rightPtr -= 1
                        while rightPtr > -1 and nums[rightPtr] == nums[rightPtr + 1]:
                            rightPtr -= 1
                    elif temp > target:
                        rightPtr -= 1
                        while rightPtr > -1 and  nums[rightPtr] == nums[rightPtr + 1]:
                            rightPtr -= 1
                    else:
                        leftPtr += 1
                        while leftPtr < nLen and nums[leftPtr] == nums[leftPtr - 1]:
                            leftPtr += 1
        return res
