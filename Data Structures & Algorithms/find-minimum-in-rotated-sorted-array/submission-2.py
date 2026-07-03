class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # find cases where the left side is bad
                if nums[l] > nums[r]:# means go right
                    l = m + 1
                else:
                    r = m - 1
            else: # went right
                if nums[m] > nums[l] or nums[m] < nums[r]: # gotta go left because the min in right sorted array is greater than the left
                    r = m - 1
                else:
                    l = m + 1
        return res
