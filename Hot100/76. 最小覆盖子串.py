import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == None or t == None or len(s) < len(t):
            return ""
        dictori = {}
        dictcur = {}
        for i in range(len(t)):
            if t[i] in dictori:
                dictori[t[i]] += 1
            else:
                dictori[t[i]] = 1
            dictcur[t[i]] = 0
        minLen = sys.maxsize
        left = right = 0
        minIndex = 0
        def check():
            for k, v in dictori.items():
                if dictcur[k] < v:
                    return False
            return True 
        while right < len(s):
            if s[right] in dictcur:
                dictcur[s[right]] += 1
                if check():
                    while left < len(s):
                        if s[left] in dictori:
                            if dictcur[s[left]] > dictori[s[left]]:
                                dictcur[s[left]] -= 1
                                left += 1
                            else:
                                break
                        else:
                            left += 1
                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        minIndex = left
                    while left < len(s):
                        if s[left] in dictcur:
                            if not check():
                                break
                            dictcur[s[left]] -= 1
                            left += 1
                        else:
                            left += 1
                right += 1 
            else:
                right += 1
        if minLen == sys.maxsize:
            return ""
        return s[minIndex: minIndex + minLen]
