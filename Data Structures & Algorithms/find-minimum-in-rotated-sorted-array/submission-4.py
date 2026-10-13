class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: # its on the right (min is on the right)
                l = mid + 1
            else: # min is on the left
                r = mid 

        return nums[l]
