class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        l, r = 0, n - 1

        while l < r:

            mid = (l + r) // 2

            if mid % 2 == 1: # force it to be the first index of a pontential pair
                mid -= 1
            
            if nums[mid] == nums[mid + 1]: # the right window is odd (contains the single element)
                l = mid + 2
            else: # the left window contains the element
                r = mid 
            
        return nums[l]


