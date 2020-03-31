/*
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
*/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        temp = [x[:] for x in board]
        
        for i in range(n):
            for j in range(m):
                # print(self.check(temp, i, j))
                board[i][j] = self.check(temp, i, j)
                
        # print(temp)        
 

        
    def check(self, board, i, j):
        
        n = len(board)
        m = len(board[0])
        num = 0
        CNT = 0
        
        if j - 1 >= 0:
            # print(i,j-1, board[i][j-1])
            num += board[i][j-1]
            # CNT = CNT + 1
        if j + 1 < m:
            # print(i,j+1, board[i][j+1])
            num += board[i][j+1]
            CNT = CNT + 1
            
        if i - 1 >= 0:
            # print(i-1,j, board[i-1][j])
            num += board[i-1][j]
            # CNT = CNT + 1
            if j - 1 >= 0:
                # print(i-1,j-1, board[i-1][j-1])
                num += board[i-1][j-1]
                # CNT = CNT + 1
            if j + 1 < m:
                # print(i-1,j+1, board[i-1][j+1])
                num += board[i-1][j+1] 
                # CNT = CNT + 1
            
        if i + 1 < n:
            # print(i+1,j,board[i+1][j])
            num += board[i+1][j]
            # CNT = CNT + 1
            if j - 1 >= 0:
                # print(i+1,j-1,board[i+1][j-1])
                num += board[i+1][j-1]
                # CNT = CNT + 1
            if j + 1 < m:
                # print(i+1,j+1,board[i+1][j+1])
                num += board[i+1][j+1] 
                # CNT = CNT + 1
            
            
        res = None  
        if board[i][j]:
            if num < 2 or num > 3:
                res = 0
            else:
                res = 1
        else:
            if num == 3:
                res = 1
            else:
                res = 0
        # print(i, j, CNT, board[i][j], num, res)
        return res
            
