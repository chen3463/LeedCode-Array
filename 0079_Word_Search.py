'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        res = False
 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.DFS(board, i, j, 0, word):
                
                    return True
                
        return False
    
    def DFS(self, board : List[List[str]], i: int, j: int, count: int, word: str) -> bool:
        if count == len(word):
            return True
        if (i < 0 or i >= len(board) or j < 0  or j >= len(board[i]) or board[i][j] != word[count]):   
            return False
        
        
        temp = board[i][j]
        board[i][j] = " "
        
        res = self.DFS(board, i+1, j, count+1, word) or self.DFS(board, i-1, j, count+1, word) or self.DFS(board, i, j+1, count+1, word) or self.DFS(board, i, j-1, count+1, word)
        
        board[i][j] = temp
        
        return res
