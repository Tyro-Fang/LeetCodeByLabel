class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        def helper(leftLens, rightLens, n, strs, res):
            if len(strs) == 2*n:
                res.append(strs)
                return
            if leftLens == 0 or leftLens == rightLens:
                strs += '('
                leftLens += 1
                helper(leftLens, rightLens, n, strs, res)
            elif leftLens == n:
                strs += ')'
                rightLens += 1
                helper(leftLens, rightLens, n, strs, res)
            else:
                strs += '('
                leftLens += 1
                helper(leftLens, rightLens, n, strs, res)
                strs = strs[:-1]
                strs += ')'
                leftLens -= 1
                rightLens += 1
                helper(leftLens, rightLens, n, strs, res)
        res = []
        helper(0, 0, n, '', res)
        return res
                

