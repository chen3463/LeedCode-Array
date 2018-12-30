# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        re = []
        for interval in intervals:
            if not re or re[-1].end < interval.start:
                re.append(interval)
            else:
                re[-1].end = max(re[-1].end, interval.end)
        return re 
