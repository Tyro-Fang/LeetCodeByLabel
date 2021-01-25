class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n :
            return 0
        dp =[[1] * n] +[[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]