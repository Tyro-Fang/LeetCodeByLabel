class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        sLen = len(s)
        maxLen = 0
        curLen = 0
        leftPtr = 0
        rightPtr = 1
        window = set()
        for i in range(sLen):
            curLen += 1
            while s[i] in window:
                window.remove(s[leftPtr])
                leftPtr += 1
                curLen -= 1
            window.add(s[i])
            maxLen = max(maxLen, curLen)
        return maxLen
