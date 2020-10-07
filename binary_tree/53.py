
指针遍历法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        numsLength = len(nums)
        sum = 0
        result = -sys.maxsize - 1
        end =  0
        while end < numsLength:
            sum += nums[end]
            if result < sum :
                result = sum
            end += 1
            if sum < 0 and end < numsLength: 
                sum = 0
        return result
            
//分治法
class ResultType:
    def __init__(self, leftSum, rightSum, maxSum, allSum):
        self.leftSum = leftSum
        self.rightSum = rightSum
        self.maxSum = maxSum
        self.allSum = allSum
class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        numsLenghth = len(nums)
        return self.divideAndConquer(nums, 0, numsLenghth - 1).maxSum
    def divideAndConquer(self, nums, start, end):
        if start == end:
            return ResultType(nums[start], nums[start], nums[start], nums[start])
        mid = start + (end - start) // 2
        leftResult = self.divideAndConquer(nums, start, mid)
        rightResult = self.divideAndConquer(nums, mid + 1, end)
        return self.calculateResult(leftResult, rightResult)
    def calculateResult(self, leftResult, rightResult):
        allSum = leftResult.allSum + rightResult.allSum
        leftSum = max(leftResult.leftSum, leftResult.allSum + rightResult.leftSum)
        rightSum = max(rightResult.rightSum, rightResult.allSum + leftResult.rightSum)
        maxSum = max(max(leftResult.maxSum, rightResult.maxSum), leftResult.rightSum + rightResult.leftSum)
        return ResultType(leftSum, rightSum, maxSum, allSum)
                