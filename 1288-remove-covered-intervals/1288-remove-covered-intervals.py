class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j:
                    if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                        ans.add(i)
        return len(intervals) - len(ans)