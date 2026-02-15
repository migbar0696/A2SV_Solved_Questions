class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        rowl = len(mat)
        coll = len(mat[0])


        if mat == target:
            return True
        
        k = 0
        while k < 3:

            for i in range(rowl):
                for j in range(i, coll):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for rows in mat:
                rows.reverse()

            if mat == target:
                return True
            k += 1
        
        return False
