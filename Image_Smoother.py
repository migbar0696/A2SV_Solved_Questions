class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        rowlm = len(img)
        colln = len(img[0])
        setpair = set()
        new_img = []

        for i in range(rowlm):
            temp = [0] * colln
            new_img.append(temp)


        for i in range(rowlm):
            for j in range(colln):
                setpair.add((i, j))
        
        
        for i in range(rowlm):

            for j in range(colln):
                sumn = img[i][j]
                cnt = 1
                if (i + 1, j) in setpair:
                    sumn += img[i +1][j]
                    cnt +=1
                if (i - 1, j) in setpair:
                    sumn += img[i - 1][j]
                    cnt += 1
                if (i, j + 1) in setpair:
                    sumn += img[i][j + 1]
                    cnt += 1
                if (i, j - 1) in setpair:
                    sumn += img[i][ j - 1]
                    cnt += 1
                if (i + 1, j + 1) in setpair:
                    sumn += img[i + 1] [j + 1]
                    cnt += 1
                if (i - 1, j - 1) in setpair:
                    sumn += img[i - 1][j - 1]
                    cnt += 1
                if (i - 1, j + 1) in setpair:
                    sumn += img[i - 1][j + 1]
                    cnt += 1
                if (i + 1, j - 1) in setpair:
                    sumn += img[i + 1][j - 1]
                    cnt += 1
                new_img[i][ j] = sumn  // cnt 
            
        return new_img
            
                



