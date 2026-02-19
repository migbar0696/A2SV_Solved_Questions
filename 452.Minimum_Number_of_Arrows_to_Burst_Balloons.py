class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        cnt = 0
        n = len(points)
        i = 0

        print(points)
        while i < n:
            j = i + 1
            minr = points[i][1]
            while j < n and  minr >= points[j][0]:
                
                if j < n and minr > points[j][1]:
                    minr = points[j][1]
                j += 1

            cnt += 1
            i = j 
                 
        return cnt
