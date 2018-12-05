class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        L = []
        
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row)-1):
                row[j] = L[i-1][j-1] + L[i-1][j]
            
            L.append(row)
        
        return L
