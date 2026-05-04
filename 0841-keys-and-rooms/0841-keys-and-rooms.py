class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False for _ in range(len(rooms))]

        queue = deque()
        queue.append(0)
        visited[0] = True
        sets = set()
        cnt = 1
        while queue:
            node = queue.popleft()
            # print(node)
            for neighbour in rooms[node]:
                if not visited[neighbour] :
                    visited[neighbour] = True
                    queue.append(neighbour)
                    sets.add(neighbour )
                    cnt += 1
                    # print(node)
        anoset = set()

        for each in rooms:
            for all in each:
                if all != 0:
                    anoset.add(all)
        # print(sets)
        # print(anoset)
        
        print(cnt, len(rooms))
        return cnt == len(rooms)
