'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

# python 2
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix) # rows
        if m > 0:
            n = len(matrix[0]) # cols
        else:
            return matrix
        l = 0 # start row index
        r = 0 # start col index
        res = []

        while (r < n and l < m):
            # append rows from samll index to large one
            for i in range(r,n):
                res = res + [matrix[l][i]]
            l = l + 1 # for next appending
            # append cols from samll index to large one
            for i in range(l,m): 
                res = res + [matrix[i][n-1]]
            n = n - 1  # for next appending
            # append rows from large index to small one
            if (l < m):
                for i in range(n-1, r-1, -1):
                    res = res + [matrix[m-1][i]]
                m = m - 1 # for next appending
            # append cols from large index to small one
            if (r < n): # for next appending
                for i in range(m-1, l-1, -1):
                    res = res + [matrix[i][r]]
                r = r + 1
                
        return res
   
# Python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return matrix
        
        n = len(matrix) # row number
        p = len(matrix[0]) # column number
        i = 0 # row index
        j = 0 # column index
        re = []
        while True:
            if p > 0 and j < p and i < n:
                re += matrix[i][j:p]
                i = i + 1
            else:
                break
                
            if n > i and p > 0:
                for k in range(i, n):
                    re += [matrix[k][p-1]]
                p = p - 1
            else:
                break
                
            if p > j and n > 0:
                for k in range(p-1,j-1,-1):
                    re += [matrix[n-1][k]]
                n = n - 1
            else:
                break
                
            if n > 0 and n > j:
                for k in range(n-1,i-1,-1):
                    re += [matrix[k][j]]
                j = j + 1
            else:
                break
                
        return re
