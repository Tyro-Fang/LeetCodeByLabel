class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closedVal = 9999999
        for i in range(len(nums) - 2):
            leftPtr = i + 1
            rightPtr = len(nums) - 1
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            maxVal = nums[i] + nums[-1] + nums[-2]
            minVal = nums[i] + nums[i + 1] + nums[i + 2]
            if maxVal < target:
                if abs(target - maxVal) < abs(target - closedVal):
                    closedVal = maxVal
                    continue
            if minVal > target:
                if abs(target - minVal) < abs(target - closedVal):
                    closedVal = minVal
                    break
            while leftPtr < rightPtr:
                temp = nums[i] + nums[leftPtr] + nums[rightPtr]
                if abs(target - temp) < abs(target - closedVal):
                    closedVal = temp
                if temp < target:
                    leftPtr += 1
                elif temp > target:
                    rightPtr -= 1
                else:
                    return target
        return closedVal

