class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        d = []
        for i in range(len(candidates)):
            if candidates[i] < target:
                for sub in self.combinationSum(candidates[i:], target-candidates[i]):
                    d.append([candidates[i]]+sub)
            elif target == candidates[i]:
                d.append([candidates[i]])
                
        return d
