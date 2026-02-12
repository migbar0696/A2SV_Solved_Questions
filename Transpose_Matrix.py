class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rowl = len(matrix)
        coll = len(matrix[0])
        transmat = []

        for i in range(coll):
            temp = [0] * rowl
            transmat.append(temp)
        
        for row in range(rowl):
            for col in range(coll):
                transmat[col][row] = matrix[row][col]
        
        return transmat
