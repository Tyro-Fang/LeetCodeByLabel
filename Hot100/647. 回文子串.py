class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        dp = [[0] * len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s)):
            dp[i][i] = 1
            count += 1
        for i in range(1, len(s)):
            for j in range(len(s) - i):
                if s[j] == s[j + i]:
                    if i == 1:
                        dp[j][j + i] = 1
                        count += 1
                    else:
                        dp[j][j + i] = dp[j + 1][j + i - 1]
                        if dp[j][j + i]:
                            count += 1
                else:
                    dp[j][j + i] = 0
        return count

