class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dictn = defaultdict(int)
        for a, b in edges:
            dictn[a] += 1
            dictn[b] += 1
        
        maxn = max(dictn.values())

        for key in dictn.keys():
            if dictn[key] == maxn:
                return key