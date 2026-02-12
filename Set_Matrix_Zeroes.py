class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setrow = set()
        setcol = set()

        rowl = len(matrix)
        coll = len(matrix[0])

        for row in range(rowl):
            for col in range(coll):
                if matrix[row][col] == 0:
                    setrow.add(row)
                    setcol.add(col)

        for rows in setrow:
            for cols in range(coll):
                matrix[rows][cols] = 0
        
        for cols in setcol:
            for rows in range(rowl):
                matrix[rows][cols] = 0
        return matrix
