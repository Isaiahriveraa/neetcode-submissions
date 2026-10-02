class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        def findClosestVal(x): # find the closest val near x
            l, r = 0, len(arr) # because we are 

            while l < r:

                mid = (l + r) // 2

                if arr[mid] >= x: # might be the valid answer so we just do mid
                    r = mid
                else:
                    l = mid + 1
                
            return l
            
        closest_index = findClosestVal(x)
        l, r = closest_index - 1, closest_index # find our bounds

        while r - l - 1 < k:
            if l < 0: # no elements left on the left, take from the right
                r += 1
            elif r >= len(arr): # no elements left on the right, take from the left
                l -= 1
            else:
                a, b = arr[l], arr[r]
                if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
                    # a is closer include it
                    l -= 1
                else: 
                    # b is closer, include this index
                    r += 1
        
        return arr[l + 1:r] # l + 1 because l is before the wanted start position

        
