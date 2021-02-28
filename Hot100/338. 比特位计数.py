class Solution:
    def countBits(self, num: int) -> List[int]:
        if not num:
            return [0]
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1 ] + (i & 1)
        return dp
