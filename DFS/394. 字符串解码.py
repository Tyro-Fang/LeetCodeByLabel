class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        index = 0
        elementsStack = []
        result = ""
        while index < len(s):
            if ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
                start = index
                index = self.getNum(s, index)
                temp = int(s[start : index])
                elementsStack.append(temp)
            elif s[index] == '[':
                elementsStack.append(s[index])
                index += 1
            elif self.isChar(s[index]):
                start = index
                index = self.getStr(s, index)
                temp = str(s[start : index])
                elementsStack.append(temp)
            elif s[index] == ']':
                elementsStack.append(self.getRes(elementsStack))
                index += 1
        while elementsStack != []:
            result = elementsStack.pop() + result
        return result
         
    def getNum(self, s, index):
        index += 1
        while index <len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
            index += 1
        return index
    
    def isChar(self, oneChar):
        if not oneChar:
            return False
        if (ord(oneChar) >= ord('A') and ord(oneChar) <= ord('Z')) or (ord(oneChar) >= ord('a') and ord(oneChar) <= ord('z')):
            return True
        return False

    def getStr(self, s, index):
        index += 1
        while index < len(s) and self.isChar(s[index]) :
            index += 1
        return index

    def getRes(self, elementsStack):
        res = ""
        temp = elementsStack.pop()
        while temp != '[' and elementsStack!= [] :
            res = temp + res
            temp = elementsStack.pop()
        repeat = elementsStack.pop()
        res = repeat * res
        return res
        
