class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while maxDoubles > 0 and target > 3:
            print(target, maxDoubles)
            cnt += target % (target // 2) 
            cnt += 1
            target = target//2
            maxDoubles -= 1
        print("target", target)
        if target > 1:
            cnt += target - 1
        return cnt
            
            