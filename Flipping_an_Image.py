class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rowl = len(image)
        coll = len(image[0])

        for i in range(rowl):
            for j in range(coll // 2):
                image[i][j], image[i][(coll - 1) - j] = image[i][coll - 1 - j], image[i][j]

        for i in range(rowl):
            for j in range(coll):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        return image
