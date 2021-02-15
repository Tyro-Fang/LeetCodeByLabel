class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxX = len(grid)
        maxY = len(grid[0])
        dp = [[0] * maxY for _ in range(maxX)]
        res = 0
        for i in range(maxX):
            for j in range(maxY):
                if dp[i][j] == 1:
                    continue
                if grid[i][j] == '1':
                    res += 1
                    self.helper(i, j, grid, dp, maxX, maxY)
        return res
        
    def helper(self, x, y, grid, dp, maxX, maxY):
        if x >= maxX or x < 0 or y >= maxY or y < 0:
            return 
        if dp[x][y] == 1:
            return 
        if grid[x][y] == '1':
            dp[x][y] = 1
            self.helper(x + 1, y, grid, dp, maxX, maxY)
            self.helper(x, y + 1, grid, dp, maxX, maxY)
            self.helper(x - 1, y, grid, dp, maxX, maxY)
            self.helper(x, y - 1, grid, dp, maxX, maxY)

