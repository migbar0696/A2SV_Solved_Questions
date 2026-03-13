class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        costs.sort(key = lambda item:abs(item[0] - item[1]), reverse = True)
        totalc = 0
        cnta = 0
        cntb = 0
        n = len(costs) // 2

        for i in range(2 * n):
            if costs[i][0] > costs[i][1]:
                totalc += costs[i][1]
                cntb += 1
            else:
                totalc += costs[i][0]
                cnta += 1
            
            if cnta == n or cntb == n:
                break
        
        if cnta ==n:
            for j in range(i + 1, 2 * n):
                totalc += costs[j][1]
        else:
            for j in range(i + 1, 2 * n):
                totalc += costs[j][0]
                
        return totalc