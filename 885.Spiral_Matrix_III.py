class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        left = cStart - 1
        right = cStart + 1
        top = rStart
        bottom = rStart + 1
        flagl = False

        res = []

        while left >=0 or right <= cols - 1 or top >= 0 or bottom <= rows - 1:

            for i in range(left + 1, right + 1):
                if top >= 0 and 0 <= i <= cols - 1:
                    res.append([top, i])
            top -= 1
            
            if flagl:
                left -= 1
            flagl = True

            for i in range(top + 2, bottom + 1):
                if right <= cols - 1 and 0 <= i <= rows - 1:
                    res.append([i, right])
            right += 1

            for i in range(right - 2, left - 1, -1):
                if bottom <= rows -1 and 0 <= i <= cols - 1 :
                    res.append([bottom, i])
            bottom += 1

            for i in range(bottom - 2, top -1, -1):
                if left >= 0 and 0 <= i <= rows - 1:
                    res.append([i, left])

        return res
         

        
