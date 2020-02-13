
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        print(len(points))
        for i in range(len(points)-1):
            dist = max(abs(points[i+1][0] - points[i][0]), abs(points[i+1][1] - points[i][1]))
            print(dist)
            time = time + dist
        return time
