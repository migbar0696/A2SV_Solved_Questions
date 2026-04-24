class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = set()

        freqbomb = defaultdict(int)

        for i in range(len(bombs)):
            node = bombs[i]
            freqbomb[tuple(node)] += 1
            for j in range(len(bombs)):
                nnode = bombs[j]
                if i != j and  node[2] >= sqrt(((node[0] - nnode[0]) ** 2 )+ ((node[1] - nnode[1])**2)) :
                    graph[tuple(node)].append(nnode)

        maxb = 0
        
        for i in range(len(bombs)):
            queue = deque([bombs[i]])
            visited = set([tuple(bombs[i])])
            cnt = freqbomb[tuple(bombs[i])]

            while queue:
                node = queue.popleft()

                for neighbour in graph[tuple(node)]:
                    if tuple(neighbour) not in visited:
                        visited.add(tuple(neighbour))
                        queue.append(neighbour)
                        cnt += freqbomb[tuple(neighbour)]
            
            maxb = max(maxb, cnt)
        return maxb




