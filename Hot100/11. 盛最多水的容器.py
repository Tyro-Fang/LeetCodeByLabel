class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        hLen = len(height)
        leftPtr = 0
        rightPtr = hLen - 1
        maxRain = 0
        while leftPtr < rightPtr:
            maxRain = max(maxRain, min(height[leftPtr], height[rightPtr]) * (rightPtr - leftPtr))
            if height[leftPtr] < height[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1
        return maxRain