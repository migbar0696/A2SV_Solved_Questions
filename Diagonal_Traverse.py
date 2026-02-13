class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        from collections import defaultdict

        dictdiagonal = defaultdict(list)
        rowl = len(mat)
        coll = len(mat[0])
        res = []

        for i in range(rowl):
            for j in range(coll):
                dictdiagonal[i + j].append(mat[i][j])
        sorted_dictdiagonal = dict(sorted(dictdiagonal.items()))
        
        for key, value in dictdiagonal.items():
            if key % 2:
                res.extend(value)
            else:
                value.reverse()
                res.extend(value)
                
        return res



# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         starti = 0
#         startj = 0
#         rowl = len(mat)
#         coll = len(mat[0])
#         setindex = set()
#         res = []

#         for i in range(rowl):
#             for j in range(coll):
#                 setindex.add((i, j))

#         parity = True

#         while (starti, startj) in setindex:
#             i = starti
#             j = startj
#             if parity:  
#                 while(i, j) in setindex:
#                     res.append(mat[i][j])
#                     i -= 1
#                     j += 1
#                 i += 1
#                 j -= 1 
#             if not parity:
#                 while(i, j) in setindex:
#                     res.append(mat[i][j])
#                     i += 1
#                     j -= 1

#                 i -= 1
#                 j += 1
            
            
#             if parity and j < coll - 1:
#                 starti = i
#                 startj = j + 1

#             elif parity and j >= coll - 1:
#                 starti = i + 1
#                 startj = j 

#             if not parity and i < rowl - 1:
#                 starti = i + 1
#                 startj = j 
#             elif not parity and i >= rowl - 1:
#                 starti = i 
#                 startj = j + 1
            
#             print(starti, startj)

#             if parity:
#                 parity = False
#             else:
#                 parity = True

#         return res
      
