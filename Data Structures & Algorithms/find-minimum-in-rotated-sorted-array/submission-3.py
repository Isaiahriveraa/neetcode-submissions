class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        l, r = 0, n - 1

        # We are not trying to land mid on the minimum 
        # We keep shrinking the window [l, r] while preserving this rule here:

        # the min is always inside the [l, r] (window)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # the values drop after the mid
                # the min must be on the right window
                l = mid + 1
            else:
                # there is not drop between the mid and the r
                # so the min is at the mid index or its somewhere to the left
                r = mid
        
        return nums[l] # I can even return nums[r] because l == r when the loop stops meaning that we shrank the window until we landed one index meaning this is the only index that satfies the answer