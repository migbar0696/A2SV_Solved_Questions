class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        rowlm = len(img)
        colln = len(img[0])
        new_img = []

        for i in range(rowlm):
            temp = [0] * colln
            new_img.append(temp)
        
        
        for i in range(rowlm):
            for j in range(colln):
                sumn = 0
                cnt = 0
                for k in range(i - 1, i + 2):
                    for z in range(j - 1, j + 2):
                        if 0 <= k <= rowlm - 1 and 0 <= z <= colln - 1:
                            sumn += img[k][z]
                            cnt += 1
                
                new_img[i][j] = sumn // cnt
        return new_img
            

# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
#         rowlm = len(img)
#         colln = len(img[0])
#         setpair = set()
#         new_img = []

#         for i in range(rowlm):
#             temp = [0] * colln
#             new_img.append(temp)


#         for i in range(rowlm):
#             for j in range(colln):
#                 setpair.add((i, j))
        
        
#         for i in range(rowlm):
#             for j in range(colln):
#                 sumn = 0
#                 cnt = 0
#                 for k in range(i - 1, i + 2):
#                     for z in range(j - 1, j + 2):
#                         if (k, z) in setpair:
#                             sumn += img[k][z]
#                             cnt += 1
                
#                 new_img[i][j] = sumn // cnt
#         return new_img
            
                                # OR

# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
#         rowlm = len(img)
#         colln = len(img[0])
#         setpair = set()
#         new_img = []

#         for i in range(rowlm):
#             temp = [0] * colln
#             new_img.append(temp)


#         for i in range(rowlm):
#             for j in range(colln):
#                 setpair.add((i, j))
        
        
#         for i in range(rowlm):

#             for j in range(colln):
#                 sumn = img[i][j]
#                 cnt = 1
#                 if (i + 1, j) in setpair:
#                     sumn += img[i +1][j]
#                     cnt +=1
#                 if (i - 1, j) in setpair:
#                     sumn += img[i - 1][j]
#                     cnt += 1
#                 if (i, j + 1) in setpair:
#                     sumn += img[i][j + 1]
#                     cnt += 1
#                 if (i, j - 1) in setpair:
#                     sumn += img[i][ j - 1]
#                     cnt += 1
#                 if (i + 1, j + 1) in setpair:
#                     sumn += img[i + 1] [j + 1]
#                     cnt += 1
#                 if (i - 1, j - 1) in setpair:
#                     sumn += img[i - 1][j - 1]
#                     cnt += 1
#                 if (i - 1, j + 1) in setpair:
#                     sumn += img[i - 1][j + 1]
#                     cnt += 1
#                 if (i + 1, j - 1) in setpair:
#                     sumn += img[i + 1][j - 1]
#                     cnt += 1
#                 new_img[i][ j] = sumn  // cnt 
            
#         return new_img
            
                



