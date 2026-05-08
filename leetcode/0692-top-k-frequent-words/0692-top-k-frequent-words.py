class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter, defaultdict

        freqw = Counter(words)

        freqarr = []
        container = defaultdict(list)

        for key, value in freqw.items():
            container[-value].append(key)
            if len(freqarr) < k:
                heappush(freqarr,value)
            elif value > freqarr[0]:
                heappushpop(freqarr,value)

        freqn = Counter(freqarr)
        
        freqarr = [ -x for x in freqn]
        heapify(freqarr)
        ans = []
        visited = set()
        print(freqarr)
        print(container)
        
        while freqarr:
            val = heappop(freqarr)

            if val not in visited:
                ans.extend(sorted(container[val])[:freqn[-val]])
                visited.add(val)
        return ans
        
        

        
