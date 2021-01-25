class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        xCount = len(grid)
        yCount = len(grid[0])
        def dfs(grid, startPos):
            grid[startPos[0]][startPos[1]] = 0
            if startPos[0] > 0:
                if grid[startPos[0] - 1][startPos[1]] == "1":
                    dfs(grid,[startPos[0] - 1,startPos[1]])
            if startPos[1] > 0:
                if grid[startPos[0]][startPos[1] - 1] == "1":
                    dfs(grid,[startPos[0],startPos[1] - 1])
            if startPos[0] < xCount - 1:
                if grid[startPos[0] + 1][startPos[1]] == "1":
                    dfs(grid,[startPos[0] + 1,startPos[1]])
            if startPos[1] < yCount - 1:
                if grid[startPos[0]][startPos[1] + 1] == "1":
                    dfs(grid,[startPos[0],startPos[1] + 1])
        for i in range(xCount):
            for j in range(yCount):
                if grid[i][j] == "1":
                    res += 1
                    dfs(grid,[i,j])
        return res

            
            