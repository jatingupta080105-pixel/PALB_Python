class Solution:
    def threeWayPartition(self, arr, a, b):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            
            # Case 1: element < a
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            
            # Case 2: element in range [a, b]
            elif a <= arr[mid] <= b:
                mid += 1
            
            # Case 3: element > b
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return True