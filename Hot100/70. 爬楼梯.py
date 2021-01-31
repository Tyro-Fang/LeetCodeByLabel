class Solution:
    def climbStairs(self, n: int) -> int:
        if not n or n == 1 or n == 2:
            return n
        last = 1
        curv = 2
        res = 0
        for i in range(3, n + 1):
            res = last + curv
            last = curv
            curv = res
        return res