#1.动态规划
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        #envelopes.sort()
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envLen = len(envelopes)
        dp = [1] * envLen
        maxNum = 1 #最大套娃数
        for i in range(1, envLen):
            tempMaxNum = 1 #对当前信封为最后一个信封的最大套娃数
            for j in range(0, i):
                if envelopes[j][1] < envelopes[i][1]:
                    tempMaxNum = max(tempMaxNum, dp[j] + 1)
            dp[i] = tempMaxNum
            maxNum = max(maxNum, tempMaxNum)
        return maxNum


#2.二分查找
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        #envelopes.sort()
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envLen = len(envelopes)
        top = [0] * envLen
        piles = 0 # 牌堆数
        for i in range(0, envLen):
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) // 2
                if top[mid] < envelopes[i][1]:
                    left = mid + 1
                else:
                    right = mid
            if left == piles:
                piles += 1
            top[left] = envelopes[i][1]
        return piles