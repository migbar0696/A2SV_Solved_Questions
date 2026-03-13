class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monds = []
        maxa = 0

        for i in range(len(heights)):
            start = i
            while monds and heights[i] < monds[-1][0]:
                maxa = max(maxa, (i - monds[-1][1]) * monds[-1][0])
                num = monds.pop()
                start = num[1]
            
            monds.append([heights[i],start])
            

        for i in range(len(monds)):
            maxa = max(maxa, monds[i][0] * (len(heights) - monds[i][1]))
        
        return maxa
