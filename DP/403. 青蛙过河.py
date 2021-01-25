class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        stonesLen = len(stones)
        dp = [set() for _ in range(stonesLen)]
        dp[0].add(0)
        for i in range(1, stonesLen):
            tempJump = set()
            for j in range(0, i):
                diff = stones[i] - stones[j]
                if diff - 1 in dp[j] or diff + 1 in dp[j] or diff in dp[j]:
                    tempJump.add(diff)
            dp[i] = tempJump
        return dp[-1] != set()



        
