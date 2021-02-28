class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return -1
        squNums = []
        i = 1
        while i * i <= n:
            squNums.append(i * i)
            i += 1
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for n in squNums:
                dp[i] = min(dp[i], dp[i - n] + 1)
        return dp[-1]



class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return -1
        squNums = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        def is_divided_by(n, count):
            if count == 1:
                return n in squNums
            for sNum in squNums:
                if is_divided_by(n - sNum, count - 1):
                    return True
            return False
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count
        
        
class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return -1
        squNums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        queue = [n]
        count = 0
        while queue:
            count += 1
            nextQueue = []
            for q in queue:
                for sNum in squNums:
                    if q - sNum == 0:
                        return count
                    elif q - sNum < 0:
                        break
                    else:
                        nextQueue.append(q - sNum)
            queue = nextQueue
        return count

        
        
