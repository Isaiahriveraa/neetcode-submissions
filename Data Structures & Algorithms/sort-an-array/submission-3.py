class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: # base case is we have one number -> we can return it back to merge with other array
            return nums

        mid = (len(nums)) // 2
        left_array = nums[:mid]
        right_array = nums[mid:]

        left_sorted_array = self.sortArray(left_array)
        right_sorted_array = self.sortArray(right_array)

        return self.merge(left_sorted_array, right_sorted_array)
        
    def merge(self, left, right):
        i = j = 0 # the starting pointers to incrementally compare to add to the merged result of both arrays
        merged = []

        while i < len(left) and j < len(right): # while both ptr's are in bounds

            if left[i] <= right[j]:
                # the number in left the pointer is referring to is less than right array's ptr (element)
                merged.append(left[i])
                i += 1 # we used this number so we 
            else: # the right element < left element
                merged.append(right[j])
                j += 1
        
        # edge case is that one of the arrays has not added all their elements
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged