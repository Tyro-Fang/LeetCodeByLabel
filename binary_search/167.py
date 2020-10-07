class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or target == None:
            return [-1,-1]
        numsLength = len(numbers)
        left = 0
        right = numsLength -1
        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left+1,right+1]
            elif result > target:
                right -= 1
            else :
                left +=1
        return [-1,-1]