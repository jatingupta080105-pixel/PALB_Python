class Solution:
    def isSubset(self, a, b):
        from collections import Counter
        
        freq = Counter(a)
        
        for num in b:
            if freq[num] > 0:
                freq[num] -= 1
            else:
                return False
        
        return True