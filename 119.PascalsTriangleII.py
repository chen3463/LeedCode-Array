class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex = rowIndex + 1

        whole = []
        for i in range(rowIndex):
            L = [None for _ in range(i+1)]
            L[0] = L[-1] = 1
            for j in range(1, len(L)-1):
                L[j] = whole[i-1][j-1] + whole[i-1][j]
                
            whole.append(L)
            
        return whole[rowIndex-1]
