class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        results = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            results[i][0] = 1
        for j in range(1, n):
            results[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                results[i][j] = results[i-1][j] + results[i][j-1]
                
        return results[-1][-1]
