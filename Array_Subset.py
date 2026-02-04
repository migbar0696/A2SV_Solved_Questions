#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        from collections import Counter
        freqa = Counter(a)
        freqb = Counter(b)
        for key, value in freqb.items():
            if value > freqa[key]:
                return False
                
        return True
    
