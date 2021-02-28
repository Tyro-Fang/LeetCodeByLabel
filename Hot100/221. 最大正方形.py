func maximalSquare(matrix [][]byte) int {
    dp := make([][]int, len(matrix))
    maxSide := 0
    for i := 0; i < len(matrix); i++ {
        dp[i] = make([]int, len(matrix[i]))
        for j := 0; j < len(matrix[i]); j++ {
            if matrix[i][j] == '1'{
                dp[i][j] = 1
                maxSide = 1
            } else{
                dp[i][j] = 0
            }
        }
    }

    for i := 1;i < len(matrix); i++ {
        for j := 1; j < len(matrix[i]); j++ {
            if dp[i][j] == 1{
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j],dp[i][j - 1])) + 1
                if dp[i][j] > maxSide{
                    maxSide = dp[i][j]
                }
            }
            
        }
    }
    return maxSide * maxSide
}

func min(a int, b int) int {
    if a < b{
        return a
    }
    return b
}