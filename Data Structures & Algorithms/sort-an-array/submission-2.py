class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        heapsort
        merge-sort
        quick-sort 
        """ 
        def mergeHalfs(arr, l, m, r):
            # need to make copies of the left and right arrays
            left, right = arr[l : m + 1], arr[m + 1: r + 1] # so we can include the r index starting pos
            i, j, k = l, 0, 0 # 0's represent the starting pos of the arr's (left -> j and our right -> k)
            while j < len(left) and k < len(right): # while the indexes are in bounds
                if left[j] <= right[k]: # if left arr num <= right arr num
                    arr[i] = left[j]
                    j += 1 #we know that each of the arrays are sorted atp and now what we want to do is we want to increment the ptr for the left subarr
                else:
                    #if arr[k] < arr[j]: 
                    arr[i] = right[k]
                    k += 1
                i += 1
            # the while loop only runs if both indexes of the subarr's are in bounds
            # edge case: if one of the array's has a greater len than the other we still need to insert those numbers into the arr
            # soltution: add the extra numbers
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
        
        def merge(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2
            merge(arr, l, m)
            merge(arr, m + 1, r)
            mergeHalfs(arr, l, m, r)
            return arr
        
        return merge(nums, 0, len(nums) - 1)
        

