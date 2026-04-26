from collections import defaultdict

class Solution:
    def countPairs(self, arr):
        freq = defaultdict(int)
        n = len(arr)
        m = len(arr[0])
        ans = 0
        
        for word in arr:
            patterns = []
            
            for i in range(m):
                pattern = word[:i] + '*' + word[i+1:]
                
                # each previous occurrence forms valid pair
                ans += freq[pattern]
                
                patterns.append(pattern)
            
            # update patterns AFTER counting
            for p in patterns:
                freq[p] += 1
        
        return ans