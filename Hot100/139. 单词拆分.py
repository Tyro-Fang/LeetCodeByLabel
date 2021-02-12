class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canMatch = [2] * len(s)
        return self.helper(s, 0, wordDict, canMatch)
        

    def helper(self, s, start, wordDict, canMatch):
        if start == len(s):
            return True
        if canMatch[start] == 1:
            return True
        elif canMatch[start] == 0:
            return False
        
        for i in range(start + 1, len(s) + 1):
            tempWord = s[start: i ]
            if tempWord in wordDict and self.helper(s, i, wordDict, canMatch):
                canMatch[start] = 1
                return True
        canMatch[start] = False
        return False



