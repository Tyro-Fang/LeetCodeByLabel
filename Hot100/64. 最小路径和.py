class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = grid[i][j] + dp[i][j - 1]
                else:
                    if j == 0:
                        dp[i][j] = grid[i][j] + dp[i - 1][j]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]