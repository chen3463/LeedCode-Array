class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        # print(rows, columns)
        
        for k in rows:
            matrix[k] = [0] * len(matrix[k])
            k = k + 1
        for h in range(len(matrix)):
            for l in columns:
                matrix[h][l] = 0
            
                
