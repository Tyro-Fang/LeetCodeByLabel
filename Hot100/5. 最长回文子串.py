#1,动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        sLen = len(s)
        dp = [[0] * sLen for _ in range(sLen)]
        # dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        startIndex  = 0
        maxLen = 1
        for i in range(sLen):
            for j in range(sLen):
                k = j + i
                if k >= sLen:
                    break
                if i == 0:
                    dp[j][k] = 1
                elif i == 1:
                    dp[j][k] = s[j] == s[k]
                elif s[j] == s[k] and dp[j + 1][k - 1]:
                    dp[j][k] = 1
                if dp[j][k] == 1 and i + 1 > maxLen:
                    startIndex = j
                    maxLen = i + 1
        return s[startIndex:startIndex + maxLen]



#2.扩散递归
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        sLen = len(s)
        maxStrs = ""
        def helper(left, right):
            while left >= 0 and right < sLen and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        for i in range(sLen):
            odd = helper(i, i)
            even = helper(i, i + 1)
            longestStrsPerStr = odd if len(odd) > len(even) else even
            if len(longestStrsPerStr) > len(maxStrs):
                maxStrs = longestStrsPerStr
        return maxStrs

        
        



