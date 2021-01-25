class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target == None:
            return False
        start = 0
        end = len(matrix) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid
            else:
                start = mid
        if matrix[start][0] == target or matrix[end][0] == target:
            return True
        if matrix[start][0] < target and target < matrix[end][0]:
            left = 0
            right = len(matrix[start]) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if matrix[start][mid] == target:
                    return True
                elif matrix[start][mid] > target:
                    right = mid
                else:
                    left = mid
            if matrix[start][left] == target:
                return True
            elif matrix[start][right] == target:
                return  True
        elif matrix[end][0] < target:
            left = 0
            right = len(matrix[end]) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if matrix[end][mid] == target:
                    return True
                elif matrix[end][mid] > target:
                    right = mid
                else:
                    left = mid
            if matrix[end][left] == target:
                return True
            elif matrix[end][right] == target:
                return  True
        return False