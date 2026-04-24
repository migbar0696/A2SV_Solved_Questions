class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])


        visiteda = [[False  for i in range(n) ] for j in range(m)]
        visitedp = [[False  for i in range(n) ] for j in range(m)]

        ansa = [[0  for i in range(n) ] for j in range(m)]
        ansp = [[0  for i in range(n) ] for j in range(m)]


        def inbound(lefti, righti):
            return 0 <= lefti < len(heights) and 0 <= righti < len(heights[0])

        

        def dfsp(lefti, righti):
            # print(lefti, righti)
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            visitedp[lefti][ righti] = True
            ansp[lefti][righti] = 1

            for leftc, rightc in direction:
                new_li = lefti + leftc
                new_ri = righti + rightc

                if inbound(new_li, new_ri) and heights[new_li][new_ri] >= heights[lefti][ righti] and not visitedp[new_li][ new_ri]:
                    dfsp(new_li, new_ri)
                    

            
        def dfsa(lefti, righti):
                # print(lefti, righti)
                direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                visiteda[lefti][ righti] = True
                ansa[lefti][righti] = 2

                for leftc, rightc in direction:
                    new_li = lefti + leftc
                    new_ri = righti + rightc
                    # print(new_li, new_ri)
                    


                    if inbound(new_li, new_ri) and heights[new_li][new_ri] >= heights[lefti][ righti] and not visiteda[new_li][ new_ri]:
                        if new_li == 0 and new_ri == 1:
                            print(lefti, righti)
                        dfsa(new_li, new_ri)

            
        for i in range(len(heights)):
            for j in range(len(heights[0])):

                if i - 1 < 0 or j - 1 < 0:
                    # print('p', i, j)
                    dfsp(i, j)
                if i == len(heights) - 1  or j == len(heights[0]) - 1:
                    # print('a', i, j)
                    dfsa(i,j)
                # print(ansp, "end","\n", )                

        # dfsa(0,0)
        # dfsp(0,0)
        # print(ansp, "end","\n")

        # print(ansa)
        # print(ansp)


        return [[x, y] for x in range(m) for y in range(n) if ansa[x][y] > 0 and ansp[x][y] > 0]