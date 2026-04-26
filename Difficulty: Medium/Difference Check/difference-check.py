class Solution:
    def minDifference(self, arr):
        def to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s
        
        times = [to_seconds(t) for t in arr]
        times.sort()
        
        n = len(times)
        min_diff = float("inf")
        
    
        for i in range(1, n):
            min_diff = min(min_diff, times[i] - times[i - 1])
        
        
        wrap_diff = (24 * 3600 - times[-1]) + times[0]
        min_diff = min(min_diff, wrap_diff)
        
        return min_diff