class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        deff = []
        maxb = 0
        minheap = []

        for i in range(1, len(heights)):
            
            deff.append((heights[i] - heights[i - 1], i))
        print(deff)
        for diff, ind in deff:
            if diff <= 0:
                maxb = max(maxb, ind)
                # print(ind)
        
            else:
                print((diff,ind))
                heappush(minheap, (diff, ind))
                ladders -= 1

                if ladders < 0:
                    val, indv = heappop(minheap)

                    if val <= bricks:
                        print(val)
                        bricks -= val
                        ladders += 1
                        maxb = max(maxb, ind)
                    else:

                        return maxb



        return len(deff)