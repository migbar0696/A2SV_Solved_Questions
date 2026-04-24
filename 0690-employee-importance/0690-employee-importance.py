"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict()

        for employee in employees:

            graph[employee.id] = employee
        
        # print(graph)

        imp = 0

        queue = deque([id])

        while queue:
            node = queue.popleft()
            imp += graph[node].importance


            for neighbour in graph[node].subordinates:
                queue.append(neighbour)
        
        return imp