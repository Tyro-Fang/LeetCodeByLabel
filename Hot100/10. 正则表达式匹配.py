class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == None or p == None:
            return False
        sLen = len(s)
        pLen = len(p)
        dp = [[False] * (pLen + 1) for _ in range(sLen + 1)]
        dp[0][0] = True
        
        for i in range(sLen + 1):
            for j in range(1, pLen + 1):
                if p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2]
                    if i > 0 and(s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                elif i == 0:
                    dp[i][j] = False
                elif p[j - 1] == '.' or s[i - 1] == p[j - 1] :
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        return dp[sLen][pLen]
        