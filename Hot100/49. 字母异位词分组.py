class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res = []
        dicts = {}
        for i in range(len(strs)):
            temp = str(sorted(strs[i]))
            if temp not in dicts:
                index = len(res)
                res.append([strs[i]])
                dicts[temp] = index
            else:
                res[dicts[temp]].append(strs[i])
        return res