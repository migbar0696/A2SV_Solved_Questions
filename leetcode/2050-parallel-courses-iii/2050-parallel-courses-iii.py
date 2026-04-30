class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = [[] for _ in range(n + 1)]
        indegree= [0 for _ in range(n + 1)]
        for pre, course in relations:
            graph[pre].append(course)
            indegree[course] += 1

        
        queue = deque()

        timen = [0] * (n + 1)
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
                timen[i] += time[i - 1]
        
        while queue:
            
            node = queue.popleft()

            for neighbour in graph[node]:
                timen[neighbour] = max(timen[neighbour], timen[node] +time[neighbour - 1] )
                
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                print(neighbour, timen[neighbour])


        return max(timen)




