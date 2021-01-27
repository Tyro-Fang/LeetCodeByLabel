# 1.双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        rains = 0
        while left <= right:
            if left_max < right_max:
                rains += max(0,left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                rains += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return rains

# 2.动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_max = []
        right_max = [0] * len(height)
        
        left_max.append(height[0])
        rains = 0
        for i in range(1, len(height) - 1):
            left_max.append(max(left_max[i - 1], height[i]))
        right_max[-1] = height[-1]
        
        for i in range(len(height) - 2, 0, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        for i in range(1, len(height) - 1):
            rains += max(min(left_max[i],right_max[i]) - height[i], 0)
        return rains
