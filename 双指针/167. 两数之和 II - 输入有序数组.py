class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or target == None:
            return [0, 0]
        leftPtr = 0
        rightPtr = len(numbers) - 1
        while leftPtr < rightPtr:
            if numbers[leftPtr] + numbers[rightPtr] == target:
                return [leftPtr + 1, rightPtr + 1]
            elif numbers[leftPtr] + numbers[rightPtr] > target:
                rightPtr -= 1
            else:
                leftPtr += 1
        return [0, 0]