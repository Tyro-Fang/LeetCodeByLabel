class Solution:
    def helper(self, board, s, word, m, haveGet):
        #s is start position
        #m is match word index
        #a is control move direction
        a = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        if m >= len(word):
            return True
        if s[0] < 0 or s[0] >= len(board) or s[1] < 0 or s[1] >= len(board[0]) or board[s[0]][s[1]] != word[m] or haveGet[s[0]][s[1]] == 1:
            return False
        isMatch = False

        haveGet[s[0]][s[1]] = 1
        for i in range(4):
            isMatch = self.helper(board, [s[0] + a[i][0], s[1] + a[i][1]], word, m + 1, haveGet)
            if isMatch:
                return True
        haveGet[s[0]][s[1]] = 0
        
        return False

    def exist(self, board, word) :
        haveGet = [[0] * len(board[0]) for _ in range(len(board))]
        if not board or not board[0] or word == None:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, [i, j], word, 0, haveGet):
                    return True
               
        return False
a = Solution()
s = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w = "ABCCED"
print(a.exist(s, w))