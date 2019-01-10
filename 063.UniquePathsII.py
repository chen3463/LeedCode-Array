class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        re = [[1 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            re[0][0] = 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                re[i][0] = 0
            else:
                re[i][0] = re[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                re[0][j] = 0  
            else:
                re[0][j] = re[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    re[i][j] = 0
                else:
                    re[i][j] = re[i-1][j] + re[i][j-1]
        return re[-1][-1]
                
