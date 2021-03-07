class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        res = x ^ y
        while res:
            if res % 2 == 1:
                count += 1
            res >>= 1
        return count
