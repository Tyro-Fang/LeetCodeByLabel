class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        if len(p) > len(s):
            return []
        dicts = {}
        res = []
        for val in p:
            if val in dicts:
                dicts[val][0] += 1
            else:
                dicts[val] = [1, 0]
        count = 0
        for i in range(len(p)):
            if s[i] in dicts:
                dicts[s[i]][1] += 1
                if dicts[s[i]][1] <= dicts[s[i]][0]:
                    count += 1
        left, right = 0, len(p) - 1
        while True:
            if count == len(p):
                res.append(left)
            if s[left] in dicts:
                dicts[s[left]][1] -= 1
                if dicts[s[left]][1] < dicts[s[left]][0]:
                    count -= 1
            left += 1
            right += 1
            if right == len(s):
                break
            if s[right] in dicts:
                dicts[s[right]][1] += 1
                if dicts[s[right]][1] <= dicts[s[right]][0]:
                    count += 1
        return res


