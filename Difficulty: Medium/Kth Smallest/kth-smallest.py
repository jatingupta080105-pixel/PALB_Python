import random

class Solution:
    def kthSmallest(self, arr, k):
        
        def quickSelect(left, right):
            pivot = arr[random.randint(left, right)]
            i, j = left, right
            
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            
            if left <= j and k - 1 <= j:
                return quickSelect(left, j)
            if i <= right and k - 1 >= i:
                return quickSelect(i, right)
                
            return arr[k - 1]
        
        return quickSelect(0, len(arr) - 1)