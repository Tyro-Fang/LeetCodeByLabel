class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        if len(s)%2==1:
            return False    
        leftStack = []
        def isLeft(s):
            if s == '(' or s == '{' or s == '[':
                return True
            return False
        dicts ={ ')':'(', ']':'[', '}':'{'} 
        for _, v in enumerate(s):
            if isLeft(v):
                leftStack.append(v)
            else:
                if leftStack == [] or dicts[v] != leftStack.pop():
                    return False
        return leftStack == []
                