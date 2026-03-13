class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monds = []
        maxa = 0
        num = []

        for i in range(len(heights)):
            while monds and heights[i] < monds[-1][0]:
                maxa = max(maxa, (i - monds[-1][1]) * monds[-1][0])
                num = monds.pop()
            
            if i == len(heights) - 1 and num:
                monds.append([heights[i], num[1]])
                monds.append([heights[i], i])
            elif num:
                monds.append([heights[i], num[1]])
            else:
                monds.append([heights[i], i])
            
            num = []
        
        if monds:
            lastn = monds[-1]
            for i in range(len(monds) - 1, -1, -1):
                maxa = max(maxa, (lastn[1] - monds[i][1] + 1) * monds[i][0])
        
        return maxa
