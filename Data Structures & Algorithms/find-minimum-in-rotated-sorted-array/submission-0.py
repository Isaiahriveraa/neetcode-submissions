class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Goal: Find the min in rotated array:

        Strat:
        Find which side is rotated

        Algo: binary search

        [3,4,5,6,1,2]
         ^         ^
         r = 5, l = 0 5 // 2 = 2 m = [5] nums[l] < nums[m] and nums[r] > nums[m]: go left
        """
        n = len(nums)
        l, r = 0, n - 1
        res = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            # if the left most number is < than the middle
            # and if the middle > right go right
            res = min(nums[m], res)
            if nums[l] < nums[m]: # left is sorted
                # if left > right
                if nums[m] > nums[r]: # go right
                    l = m + 1
                else:
                    r = m - 1
            else: # right is sorted if nums[m] > nums[l]
                if nums[m] < nums[r]: #if the middle < nums[r] go left
                    r = m - 1
                else:
                    l = m + 1
        
        return res