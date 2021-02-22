class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or not target:
            return False
        m = len(matrix)
        n = len(matrix[0])
        x = m - 1
        y = 0
        while True:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target :
                x -= 1
            if matrix[x][y] < target:
                y += 1
            if x < 0  or y >= n:
                return False


