class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dicts = {}
        dicts["2"] = ["a", "b", "c"]
        dicts["3"] = ["d", "e", "f"]
        dicts["4"] = ["g", "h", "i"]
        dicts["5"] = ["j", "k", "l"]
        dicts["6"] = ["m", "n", "o"]
        dicts["7"] = ["p", "q", "r", "s"]
        dicts["8"] = ["t", "u", "v"]
        dicts["9"] = ["w", "x", "y", "z"]
        res = []
        def getStr(strs, index, lens, res):
            if index == lens:
                res.append(strs)
                return
            strList = dicts[digits[index]]
            for i in range(len(strList)):
                temp = strs + strList[i]
                getStr(temp, index + 1, lens, res)
        dLen = len(digits)
        getStr("", 0, dLen, res)
        return res
        

