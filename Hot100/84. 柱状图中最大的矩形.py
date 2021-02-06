class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return -1
        res = 0
        heights = [0] + heights + [0]
        hLen = len(heights)
        stack = [0]
        for i in range(1, hLen):
            while stack and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res

                
            