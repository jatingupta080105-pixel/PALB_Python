class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        # Function to calculate next gap
        def nextGap(gap):
            if gap <= 1:
                return 0
            return (gap // 2) + (gap % 2)
        
        gap = nextGap(n + m)
        
        while gap > 0:
            i = 0
            j = gap
            
            while j < (n + m):
                
                # Case 1: both in a[]
                if i < n and j < n:
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                
                # Case 2: i in a[], j in b[]
                elif i < n and j >= n:
                    if a[i] > b[j - n]:
                        a[i], b[j - n] = b[j - n], a[i]
                
                # Case 3: both in b[]
                else:
                    if b[i - n] > b[j - n]:
                        b[i - n], b[j - n] = b[j - n], b[i - n]
                
                i += 1
                j += 1
            
            gap = nextGap(gap)