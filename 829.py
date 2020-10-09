class Solution:
    #双指针法，会超时
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == None or N <= 0:
            return -1
        if N == 1:
            return 1
        start = 1
        end = start + 1
        temp = start
        count = 0
        while start <= N // 2 :
            if temp < N:
                temp += end
                end += 1
            elif temp > N:
                temp -= start
                start += 1
            else:
                count += 1
                temp -= start
                start += 1
        return count + 1