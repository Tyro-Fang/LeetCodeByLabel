class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return T
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            if not stack:
                stack.append([T[i], i])
            else:
                if T[i] < stack[-1][0]:
                    stack.append([T[i], i])
                else:
                    while stack and T[i] > stack[-1][0]:
                        tempVal = stack.pop()
                        res[tempVal[1]] = i - tempVal[1]
                    stack.append([T[i], i])
        return res
                
