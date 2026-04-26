import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2
        
        # max heap (use negative values)
        heap = [-x for x in arr]
        heapq.heapify(heap)
        
        ops = 0
        
        while total > target:
            # get largest
            x = -heapq.heappop(heap)
            
            # remove its contribution
            total -= x
            
            # halve it
            x = x / 2
            
            # add back
            total += x
            heapq.heappush(heap, -x)
            
            ops += 1
        
        return ops