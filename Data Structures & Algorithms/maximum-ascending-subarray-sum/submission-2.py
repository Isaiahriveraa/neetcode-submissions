class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        """
        Given an array of positive ints nums
        return the max possible sum of an strictly increaing subarry in nums
        """

        max_sum = 0
        l = 0
        cur_sum = 0

        for r, n in enumerate(nums):
            """
            nums=[12,17,15,13,10,11,12]
                  0   1  2  3  4  5  6
                  l      r
                cur_sum = 29 - 12 - 17= 0 = 15
                max_sum = 29

            """

            # if the prev is greater than the  current we must remove from the left
            if r - 1 >= 0 and nums[r] <= nums[r - 1]:
                cur_sum = 0
                l = r
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        
        return max_sum