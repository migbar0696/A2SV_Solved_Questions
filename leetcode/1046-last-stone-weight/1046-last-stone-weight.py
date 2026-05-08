class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) >= 2:
            x = -heappop(stones)
            y = -heappop(stones)
            print(x, y)

            if x - y > 0:
                heappush(stones, y - x)

        return -stones[0] if stones else 0


